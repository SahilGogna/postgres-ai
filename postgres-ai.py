from langchain_community.chat_models import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
import streamlit as st

# Connect to your Postgres DB
db = SQLDatabase.from_uri("postgresql+psycopg2://sahil:sahil@localhost:5433/postgres")

# Connect to the local LLM (like mistral or llama3 via Ollama)
llm = ChatOllama(model="llama3.2")  # or "llama3", "llama2", etc.

# Create the SQL query chain
chain = create_sql_query_chain(llm, db)

st.title("Ask your Postgres DB (LLM-powered)")
question = st.text_input("Enter your question:")

if question:
    with st.spinner("Thinking..."):
        try:
            response = chain.invoke({"question": question})
            st.code(response, language="sql")
        except Exception as e:
            st.error(f"Error: {e}")
