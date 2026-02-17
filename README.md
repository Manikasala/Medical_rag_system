# Medical_rag_system
A production-ready local AI application that reads patient PDF reports, understands diseases and medicines, retrieves verified medical knowledge using RAG, and generates accurate clinical answers ,all running fully offline with zero API 

# Project Overview
This project solves the problem of extracting reliable medical insights from unstructured patient PDF reports and clinical documents. Traditional chatbots generate generic answers, but they do not reference verified medical sources. To overcome this, the system uses Retrieval-Augmented Generation (RAG) to retrieve relevant medical knowledge from a structured vector database before generating a response. This ensures answers are context-aware, evidence-grounded, and clinically relevant. The entire system runs fully offline, making it secure for handling sensitive patient data without relying on external APIs or cloud services.

# System Architecture
[Medical RAG Architecture](architecture.png)

# Sample Outputs
Patient Report Q&A[Output 1](outputs/output1.jpeg)

# Disease Explanation
[Output 2](outputs/output2.jpeg)

# Clinical Insight Generation
[Output 3](outputs/output3.jpeg)

# How It Works (Step-by-Step Flow)
1. User uploads medical PDF
2. Loader extracts text
3. Text is chunked
4. Embeddings are created
5. Stored in vector database
6. User asks question
7. Relevant chunks retrieved
8. LLM generates answer using context

# Tech Stack:-
- Python
- LangChain
- FAISS
- Sentence Transformers
- Streamlit
- Local LLM (Ollama / Mistral)

# How to Run:-
pip install -r requirements.txt

streamlit run app.py


