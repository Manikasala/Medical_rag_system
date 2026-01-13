import streamlit as st
import os
from loader import load_pdf
from vector_store import create_db, load_db
from rag_chain import get_rag_chain

st.set_page_config(page_title="Medical Deep Agent")
st.title("🧠 Medical Deep-Agent RAG Assistant")

file = st.file_uploader("Upload Medical PDF", type="pdf")

if file:
    os.makedirs("data/uploads", exist_ok=True)
    file_path = f"data/uploads/{file.name}"

    with open(file_path, "wb") as f:
        f.write(file.getbuffer())

    docs = load_pdf(file_path)
    create_db(docs)
    st.success("PDF indexed successfully!")

query = st.text_input("Ask medical question")

if query:
    db = load_db()
    rag_chain = get_rag_chain(db)
    answer = rag_chain.invoke(query)
    st.write("### 🩺 AI Response")
    st.write(answer)
