# 🧠 Postgres AI Query App with LangChain + Ollama

This app allows you to query a PostgreSQL database using natural language, powered by a **local LLM** (like `mistral`, `llama2`, or `llama3`) via [Ollama](https://ollama.com) and [LangChain](https://www.langchain.com/).  
No OpenAI key needed. All offline. All yours.

---

## 📦 Features

- 🧾 Natural Language to SQL
- 🔐 100% Local – No external API calls
- 🐘 Connects to PostgreSQL via SQLAlchemy
- 🧠 Uses LangChain + Ollama for local LLM inference

---

## ⚙️ Requirements

- Python 3.10+
- PostgreSQL (running locally)
- [Ollama installed](https://ollama.com/download)
- A local LLM (e.g., `mistral`, `llama2`, or `llama3`)

---

## 📥 Install Dependencies

```bash
pip install langchain langchain-community langchain-openai psycopg2-binary

---

## Setup & Installation

```bash
# Install dependencies
pip install langchain langchain-community langchain-openai psycopg2-binary

# Install Ollama (macOS example)
brew install ollama

# Start Ollama server
ollama serve

# Pull a model
ollama pull mistral

# Run it to test
ollama run mistral
---
## 📥 Install Dependencies

```bash
streamlit run app.py
