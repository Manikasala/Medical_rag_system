from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

DB_PATH = "faiss_db"

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_db(docs):
    if not docs:
        raise ValueError("No content found in PDF")
    db = FAISS.from_documents(docs, get_embeddings())
    db.save_local(DB_PATH)

def load_db():
    if not os.path.exists(DB_PATH):
        raise ValueError("No vector DB found. Upload PDF first.")
    return FAISS.load_local(DB_PATH, get_embeddings(), allow_dangerous_deserialization=True)
