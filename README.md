# 🤖 Seora Assistance

Seora Assistance is an AI-powered chatbot built using **LangChain**, **Groq LLM**, and **Streamlit**.  
It provides a conversational interface where users can interact with an AI assistant and receive helpful, concise, and intelligent responses.

The project demonstrates the implementation of a modern LLM-based chatbot using message-based conversations, prompt engineering, and session-based chat memory.

---

## 🚀 Features

- 💬 Interactive chat interface using Streamlit
- 🧠 Powered by Large Language Models (LLM)
- 🔗 Built with LangChain framework
- ⚡ Uses Groq API for fast inference
- 📝 Custom system prompt for assistant behavior
- 🗂️ Maintains conversation history during the session
- 🔐 Secure API key management using environment variables

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Frameworks & Libraries
- LangChain
- LangChain Groq
- Streamlit
- Python-dotenv

### AI Model
- Llama 3.1 8B Instant (via Groq)

---

## 📂 Project Structure

```
seora-assistance/
│
├── app/
│   ├── main.py          # Main Streamlit application
│   ├── models.py        # LLM model configuration
│   └── prompts.py       # System prompts and chatbot instructions
│
├── .env                 # Environment variables (API keys)
├── .gitignore           # Git ignored files
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/MuizSarwar/seora-assistance.git
```

Navigate into the project:

```bash
cd seora-assistance
```

---

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/Mac**

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Groq API key.

---

## ▶️ Run the Application

From the project root directory:

```bash
streamlit run app/main.py
```

The application will open in your browser.

---

## 🧩 How It Works

1. User enters a message through the Streamlit chat interface.
2. The message is converted into a LangChain `HumanMessage`.
3. Previous conversation history is stored using Streamlit session state.
4. The conversation history is sent to the LLM.
5. The model generates a response.
6. The response is displayed and stored as an `AIMessage`.

---

## 🏗️ Future Improvements

Planned improvements:

- [ ] Add Retrieval-Augmented Generation (RAG)
- [ ] Add PDF and document chat support
- [ ] Implement vector database integration (FAISS/ChromaDB)
- [ ] Add long-term conversation memory
- [ ] Add multiple LLM model support
- [ ] Add voice input/output
- [ ] Improve UI design
- [ ] Deploy the application online

---

## 👨‍💻 Author

**Muiz Sarwar**

- GitHub: [MuizSarwar](https://github.com/MuizSarwar)
