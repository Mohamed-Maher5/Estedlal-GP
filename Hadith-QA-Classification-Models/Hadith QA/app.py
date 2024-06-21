import os
import re
import gradio as gr
import qdrant_client
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant
from langchain_google_genai import ChatGoogleGenerativeAI

class HadithChatApp:
    def __init__(self):
        self.QDRANT_URL = os.getenv('QDRANT_URL')
        self.QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
        self.GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

        self.collection_name = "Cluster0"

        self.client = qdrant_client.QdrantClient(
            url=self.QDRANT_URL,
            api_key=self.QDRANT_API_KEY
        )

        self.embeddings = HuggingFaceEmbeddings(
            model_name="intfloat/multilingual-e5-small"
        )

        self.vectorStore = Qdrant(
            client=self.client,
            collection_name=self.collection_name,
            embeddings=self.embeddings
        )

        self.chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest",google_api_key=self.GOOGLE_API_KEY)

    def clean_text(self, text):
        text = re.sub(r'<[^>]*>', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text)
        return text.lower().strip()

    def get_relevant_docs(self, question, k):
        relevant_docs = self.vectorStore.similarity_search_with_score(query=question, k=k)
        return relevant_docs

    def extract_contexts(self, relevant_docs):
        contexts = []
        for doc in relevant_docs:
            contexts.append(doc[0].page_content)
        return contexts

    def create_template(self, question, k):
        relevant_docs = self.get_relevant_docs(question, k)
        contexts = self.extract_contexts(relevant_docs)
        template = f"""
        Engage in a conversation with the user, responding to their question:
        {question}
        within this contexts of Hadiths:
        {contexts} 
        Encourage the model to provide informative and culturally sensitive answers, reflecting Islamic teachings. Maintain a conversational tone and aim for clarity in responses and make sure they are restricted extracted from the provided contexts and i want you to answer me in arabic."""
        return template

    def generate_answer(self, question):
        cleaned_question = self.clean_text(question)
        query = self.create_template(cleaned_question, 10)
        response = self.clean_text(self.chat.invoke(query).content)
        return response

    def greet(self, question):
        answer = self.generate_answer(question)
        return answer
    
if __name__ == "__main__":
    # Initialize the app
    hadith_chat_app = HadithChatApp()

    # Set up the Gradio interface
    iface = gr.Interface(
        fn=hadith_chat_app.greet,
        inputs="text",
        outputs="text",
        title="Hadith QA App"
    )

    # Launch the Gradio interface
    iface.launch()