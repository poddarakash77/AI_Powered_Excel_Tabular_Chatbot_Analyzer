from langchain.chat_models import init_chat_model
from langchain_openai import OpenAIEmbeddings
import streamlit as st

from config import load_api_key
from dataloader import load_file
from prompt import get_prompt_template
from rag_engine import load_retriever, generate_answer

api_key = load_api_key()
llm = init_chat_model("gpt-4o-mini", model_provider="openai")
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
prompt = get_prompt_template()

st.title("CHATBOT")
with st.sidebar:
    st.header("Upload File")
    uploaded_file = st.file_uploader(
        "CSV/Excel File",
        type=["csv", "xls", "xlsx", "xlsm"]
    )

if uploaded_file:
    docs_list = load_file(uploaded_file)
    retriever = load_retriever(docs_list, embedding_model)

if not uploaded_file:
    st.warning("Please upload a file to start the chat.")
    st.stop()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
query = st.chat_input("Ask your question...")

if query:
    if query.lower() == "exit":
        st.session_state.chat_history.append(("user", query))
        st.session_state.chat_history.append(("assistant", "Session ended."))
    else:
        answer = generate_answer(query, prompt, llm, retriever, st.session_state.chat_history)
        st.session_state.chat_history.append(("user", query))
        st.session_state.chat_history.append(("assistant", answer))

for role, msg in st.session_state.chat_history:
    st.chat_message(role).write(msg)

