import os
import re
import pickle
import numpy as np
import pandas as pd
import nltk
import gradio as gr
from sklearn.metrics.pairwise import cosine_similarity

class HadithClassificationApp:
    def __init__(self):
        # Download NLTK resources if needed
        nltk.download('punkt')

        # Define file paths
        base_path = os.path.dirname(__file__)
        dataset_path = os.path.join(base_path, "Preprocessed_LK_Hadith_dataset.csv")
        vectorizer_path = os.path.join(base_path, "tfidf_vectorizer.pkl")
        similarity_model_path = os.path.join(base_path, "cosine_similarity_model.pkl")

        # Load the dataset and labels
        self.dataset = pd.read_csv(dataset_path)
        self.labels = self.dataset['Arabic_Grade']

        # Load the models
        with open(vectorizer_path, "rb") as f:
            self.vectorizer = pickle.load(f)
        with open(similarity_model_path, "rb") as f:
            self.X = pickle.load(f)

    @staticmethod
    def remove_tashkeel(text):
        tashkeel_pattern = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
        return re.sub(tashkeel_pattern, '', text)

    def preprocess_arabic_text(self, text):
        text = self.remove_tashkeel(text)
        tokens = nltk.word_tokenize(text)
        cleaned_tokens = [token for token in tokens if token.isalnum()]
        lowercase_tokens = [token.lower() for token in cleaned_tokens]
        return " ".join(lowercase_tokens)

    def predict_label(self, input_text, threshold=0.5):
        input_text = self.preprocess_arabic_text(input_text)
        input_vector = self.vectorizer.transform([input_text])
        similarities = cosine_similarity(input_vector, self.X).flatten()

        max_index = np.argmax(similarities)
        max_similarity = similarities[max_index]

        if max_similarity >= threshold:
            return self.labels.iloc[max_index]
        else:
            return "No similar text found in dataset"

    def classify_hadith(self, input_text):
        return self.predict_label(input_text)

if __name__ == "__main__":
    # Initialize the app
    hadith_classification_app = HadithClassificationApp()

    # Set up the Gradio interface
    iface = gr.Interface(
        fn=hadith_classification_app.classify_hadith,
        inputs="text",
        outputs="text",
        title="Hadith Classification App",
    )

    # Launch the Gradio interface
    iface.launch()