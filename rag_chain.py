from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.runnables import RunnablePassthrough

def get_rag_chain(db):
    retriever = db.as_retriever(search_kwargs={"k": 4})
    llm = Ollama(model="llama3")

    prompt = ChatPromptTemplate.from_template("""
Use the following medical context to answer the question.

Context:
{context}

Question:
{question}
""")

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    return chain
