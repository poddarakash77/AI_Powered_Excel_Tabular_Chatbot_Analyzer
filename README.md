# AI-Powered Tabular Data Analyzer

Overview
AI-Powered Tabular Data Analyzer is an advanced, AI-powered conversational chatbot designed to analyze complex tabular data (specifically financial and business metrics in Excel format). By combining the strengths of Retrieval-Augmented Generation (RAG) and powerful Large Language Models (LLMs), this system allows users to ask natural language questions about their data, receive accurate summaries, gain insights, and generate visualizations without writing any code.

1. Commands to create a virtual env using conda:
conda create -n rag-env python=3.12
conda activate rag-env

Alternative commands to create a virtual env:
python3 -m venv .venv
. ./.venv/bin/activate

2.	Go to the location of app.py file on the command prompt.
3.	Install the required packages:
pip install -r requirements.txt

4.	Run the streamlit app:
python -m streamlit run app.py

5.	(Optional) After using the application, if you are using a python virtual environment, exit the environment using below commands:
For Conda:
conda deactivate

Otherwise:
deactivate
