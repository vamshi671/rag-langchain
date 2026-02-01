# 🧠 RAG Chat Assistant (Ollama + LLaMA 3)

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions grounded strictly in the document content.

This project runs **fully locally** using **Ollama + LLaMA 3**, with **no paid APIs**.

---

## 🚀 Features
- Upload PDF documents
- Ask natural language questions
- Answers grounded in document context
- Chat-style UI using Streamlit
- Source document references
- Fully offline & private

---

## 🛠 Tech Stack
- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Ollama (LLaMA 3)

---

## 📦 Setup Instructions

### 1️⃣ Install Ollama
brew install ollama
ollama pull llama3
ollama serve
### 2️⃣ Clone Repository
git clone https://github.com/<vamshi671>/rag-langchain.git
cd rag-langchain
### 3️⃣ Create Virtual Environment
python -m venv rag-env
source rag-env/bin/activate
pip install -r requirements.txt
### 4️⃣ Run the Application
streamlit run app.py
### 5️⃣ Use the App
Upload a PDF document

Ask questions in natural language

Get answers grounded strictly in the document

View source references for transparency
