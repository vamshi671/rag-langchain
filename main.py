from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embeddings
from rag.vectorstore import create_vectorstore
from rag.qa_chain import build_qa_chain

# Load & process document
documents = load_documents("data/sample.pdf")
chunks = split_documents(documents)

embeddings = get_embeddings()
vectorstore = create_vectorstore(chunks, embeddings)

qa_chain = build_qa_chain(vectorstore)

# Ask question
query = input("Ask a question: ")
result = qa_chain(query)

print("\nAnswer:\n", result["result"])
