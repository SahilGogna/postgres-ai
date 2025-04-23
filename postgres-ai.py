from langchain_community.chat_models import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain

# Connect to your Postgres DB
db = SQLDatabase.from_uri("postgresql+psycopg2://sahil:sahil@localhost:5433/postgres")

# Connect to the local LLM (like mistral or llama3 via Ollama)
llm = ChatOllama(model="llama3.2")  # or "llama3", "llama2", etc.

# Create the SQL query chain
chain = create_sql_query_chain(llm, db)

# Ask a question!
response = chain.invoke({
    "question": "Which is the most popular membership?"
})

print(response)
