from langchain_community.chat_models import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_experimental.sql import SQLDatabaseChain
from sqlalchemy import text 
import pandas as pd

# Connect to your Postgres DB
db = SQLDatabase.from_uri("postgresql+psycopg2://sahil:sahil@localhost:5433/postgres")

# Initialize session state to keep history
if "history" not in st.session_state:
    st.session_state.history = []

# Fetch dynamic schema context
table_info = db.get_table_info()  # this gives a descriptive summary of tables, columns, types

# Custom prompt with table_info injected
custom_prompt = PromptTemplate(
    input_variables=["input", "table_info", "dialect"],
    template="""
You are an expert data analyst. Based on the input question and the table schema, return **only the SQL query** (no explanations, no commentary). 

Use only the tables and columns described below:
{table_info}

Dialect: {dialect}

Question: {input}

SQL Query:
"""
)

# Connect to the local LLM (like mistral or llama3 via Ollama)
llm = ChatOllama(model="llama3.2")

# Create the chain with dynamic table info
chain = SQLDatabaseChain(
    llm=llm,
    database=db,
    prompt=custom_prompt,
    verbose=True,
    return_intermediate_steps=True,
    return_direct=False,
    use_query_checker=False
)

st.title("Ask your Postgres DB (LLM-powered)")
question = st.text_input("Enter your question:")

if question:
    with st.spinner("Thinking..."):
        try:
            response = chain.invoke({"query": question})
            sql = response["result"]

            # st.code(sql, language="sql")

            with db._engine.connect() as conn:
                result = conn.execute(text(sql))
                rows = result.fetchall()
                columns = result.keys()

            df = pd.DataFrame(rows, columns=columns)

            # Store question and result in session state
            st.session_state.history.append({
                "question": question,
                "sql": sql,
                "result_df": df
            })
            # st.dataframe(df)
        except Exception as e:
            st.error(f"Error: {e}")
            
# Display full history (scrollable)
for item in st.session_state.history:
    st.markdown(f"**Question:** {item['question']}")
    st.code(item['sql'], language="sql")
    st.dataframe(item['result_df'])
    st.markdown("---")
