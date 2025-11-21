from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_retriever(docs_list, embedding_model):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=80
    )
    chunks = splitter.split_documents(docs_list)
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    retriever = vectorstore.as_retriever(k=5)
    return retriever

def generate_answer(query, prompt, llm, retriever, chat_history):
    rag_docs = retriever.invoke(query)
    rag_context = "\n\n".join([d.page_content for d in rag_docs])

    final_prompt = prompt.format_messages(
        rag_context=rag_context,
        query=query,
        chat_history=chat_history
    )

    response = llm.invoke(final_prompt)
    return response.content