# 🧠 RAG Chat Assistant (Ollama + LLaMA 3)

A **Retrieval-Augmented Generation (RAG)** application that allows users to **upload PDF documents** and ask questions grounded **strictly in the document content**.

🔒 Fully local & private  
⚡ Powered by **Ollama + LLaMA 3**  

---

## 🚀 Features

- 📄 Upload PDF documents
- 💬 Chat-style question answering
- 📚 Answers grounded only in uploaded documents
- 🔍 Source references with page numbers
- 🖥️ Clean Streamlit UI
- 📴 Fully offline (no paid APIs)

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Ollama (LLaMA 3)

---

## 📂 Project Structure
```text
rag-langchain/
│
├── data/                # Sample PDFs
├── demo/                # Screenshots / demo images
├── rag/                 # RAG pipeline modules
│   ├── embeddings.py
│   ├── loader.py
│   ├── splitter.py
│   ├── vectorstore.py
│   └── qa_chain.py
│
├── app.py               # Streamlit app
├── main.py              # Optional CLI / testing
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md

### 1️⃣ Install Ollama
```bash
brew install ollama
ollama pull llama3
ollama serve
```
2️⃣ Clone the Repository
```bash
git clone https://github.com/vamshi671/rag-langchain.git
cd rag-langchain
```
3️⃣ Create Virtual Environment
```bash
python -m venv rag-env
source rag-env/bin/activate
pip install -r requirements.txt
```
4️⃣ Run the Application'
```bash
streamlit run app.py
```
🐳  Docker
```bash
docker build -t rag-chat-app .
docker run -p 8501:8501 rag-chat-app
```






