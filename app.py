import streamlit as st
from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embeddings
from rag.vectorstore import create_vectorstore
from rag.qa_chain import build_qa_chain

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(page_title="RAG Chat Assistant", layout="wide")
st.title("💬 RAG Chat Assistant")
st.caption(
    "Ask questions and get answers grounded **only** in your uploaded document."
)

st.markdown("---")

# -------------------------------------------------
# Session state initialization
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.title("📄 RAG Assistant")
st.sidebar.markdown(
    "Upload a document and chat with it using **Retrieval-Augmented Generation (RAG)**."
)
st.sidebar.divider()

uploaded_file = st.sidebar.file_uploader(
    "📤 Upload PDF",
    type=["pdf"],
    help="Upload a PDF to build a searchable knowledge base"
)

@st.cache_resource
def process_document(file_path):
    documents = load_documents(file_path)
    chunks = split_documents(documents)
    embeddings = get_embeddings()
    vectorstore = create_vectorstore(chunks, embeddings)
    return build_qa_chain(vectorstore)

# -------------------------------------------------
# Handle PDF upload
# -------------------------------------------------
if uploaded_file:
    file_path = f"data/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Reset chat when new document is uploaded
    st.session_state.messages = []

    st.session_state.qa_chain = process_document(file_path)
    st.sidebar.success("✅ PDF processed successfully")

# -------------------------------------------------
# Display chat history
# -------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------------------------
# Chat input
# -------------------------------------------------
prompt = st.chat_input("Ask a question about the document")

if prompt and st.session_state.qa_chain:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = st.session_state.qa_chain(prompt)
            answer = result["result"]
            sources = result["source_documents"]

            st.markdown(answer)

            # Show sources
            with st.expander("📚 Sources used for this answer"):
                for i, doc in enumerate(sources):
                    st.markdown(f"### Source {i+1}")
                    st.markdown(
                        f"**Page:** {doc.metadata.get('page', 'N/A')}"
                    )
                    st.code(doc.page_content, language="text")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

elif prompt and not st.session_state.qa_chain:
    st.warning("⚠️ Please upload a PDF first.")
