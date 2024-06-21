document.addEventListener('DOMContentLoaded', () => {
    const chatInput = document.querySelector('#chat-input');
    const sendButton = document.querySelector('#send-btn');
    const themeButton = document.querySelector('#theme-btn');
    const deleteButton = document.querySelector('#delete-btn');
    const chatContainer = document.querySelector('.chat-container');
    let userText = null;
    const initialHeight = chatInput.scrollHeight;

    const loadDataFromLocalStorage = () => {
        chatContainer.scrollTo(0, chatContainer.scrollHeight);
        const defaultText = `<div class="default-text">
                                <h1>EstedlalChat</h1>
                                <p>Search in the hadiths using a question, research statement,
                                    phrase, or word.</p>
                            </div>`;
        chatContainer.innerHTML = localStorage.getItem("all-chats") || defaultText;
    }

    loadDataFromLocalStorage();

    const createElement = (html, className) => {
        const chatDiv = document.createElement("div");
        chatDiv.classList.add("chat", className);
        chatDiv.innerHTML = html;
        return chatDiv;
    }

    const showTypingAnimation = () => {
        const html = `<div class="chat-content">
                        <div class="chat-details">
                            <h1>Estedlal</h1>
                            <div class="typing-animation">
                                <div class="typing-dot" style="--delay: 0.2s"></div>
                                <div class="typing-dot" style="--delay: 0.3s"></div>
                                <div class="typing-dot" style="--delay: 0.4s"></div>
                            </div>
                        </div>
                        <span onclick="copyResponse(this)" class="material-symbols-rounded">content_copy</span>
                    </div>`;

        const incomingChatDiv = createElement(html, "incoming");
        chatContainer.scrollTo(0, chatContainer.scrollHeight);
        chatContainer.appendChild(incomingChatDiv);
    }

    const handleOutgoingChat = () => {
        userText = chatInput.value.trim();
        if (!userText) return;
        
        chatInput.value = "";
        chatInput.style.height = `${initialHeight}px`;

        const html = `<div class="chat-content">
                        <div class="chat-details">
                            <h1>User</h1>
                            <p>${userText}</p>
                        </div>
                    </div>`;

        const outgoingChatDiv = createElement(html, "outgoing");
        document.querySelector(".default-text")?.remove();
        chatContainer.appendChild(outgoingChatDiv);
        chatContainer.scrollTo(0, chatContainer.scrollHeight);
        setTimeout(showTypingAnimation, 500);
    }

    const copyResponse = (copyBtn) => {
        const responseTextElement = copyBtn.parentElement.querySelector("p");
        navigator.clipboard.writeText(responseTextElement.textContent);
        copyBtn.textContent = "done";
        setTimeout(() => copyBtn.textContent = "content_copy", 1000);
    }

    themeButton.addEventListener("click", () => {
        document.body.classList.toggle("light_mode");
        themeButton.innerText = document.body.classList.contains("light_mode") ? "dark_mode" : "light_mode";
    });

    deleteButton.addEventListener("click", () => {
        localStorage.removeItem("all-chats");
        loadDataFromLocalStorage();
    });

    chatInput.addEventListener("input", () => {
        chatInput.style.height = `${initialHeight}px`;
        chatInput.style.height = `${chatInput.scrollHeight}px`;
    });

    chatInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
            e.preventDefault();
            handleOutgoingChat();
        }
    });

    sendButton.addEventListener("click", handleOutgoingChat);

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
