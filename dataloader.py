import pandas as pd
import streamlit as st
from langchain_core.documents import Document

def load_file(uploaded_file):
    ext = uploaded_file.name.split(".")[-1].lower()

    if ext == "csv":
        df = pd.read_csv(uploaded_file)
        return extract_col(df)

    elif ext in ["xls", "xlsx", "xlsm"]:
        df = pd.read_excel(uploaded_file)
        return extract_col(df)

    else:
        st.error("Unsupported file type.")
        return []
    
def extract_col(df):
    normalized_cols = {col.lower(): col for col in df.columns}

    lessons_col = None
    for col in normalized_cols:
        if "lessons" in col:
            lessons_col = normalized_cols[col]
            break

    if not lessons_col:
        st.error("No Lessons column found in the uploaded file.")
        return []

    lesson_texts = df[lessons_col].dropna().astype(str).tolist()
    docs = [Document(page_content=text) for text in lesson_texts]

    return docs
