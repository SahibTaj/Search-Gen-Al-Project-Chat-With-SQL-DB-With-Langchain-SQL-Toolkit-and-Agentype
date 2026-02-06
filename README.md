# 🧠 Chat with SQL Databases using LangChain + Groq

LLM-powered natural language interface for structured databases (SQLite & MySQL)

A lightweight application that allows users to query SQL databases using natural language.
Built with LangChain agents and Groq LLM inference for fast, low-latency database reasoning.

This project demonstrates how to safely connect LLMs to production databases while enforcing query restrictions and maintaining read-only guarantees.

## 🚀 Overview

Traditional SQL querying requires technical knowledge of schema and query syntax.
This system enables conversational querying of databases using natural language while:

- Translating questions → SQL queries

- Executing queries safely

- Returning structured results

- Preventing destructive operations

- Designed as a practical foundation for:

- AI data assistants

- internal analytics tools

- business dashboards

- database copilots

## 🏗️ System Architecture

    User → Streamlit UI → LangChain SQL Agent → Groq LLM → SQL Database → Results → UI

Key components:

- LLM: Llama-3.1-8B via Groq API

- Agent: LangChain SQL Agent (ReAct reasoning)

- Database support:

- SQLite (local)

- MySQL (remote)

- Safety layer: Query restrictions enforced in agent prompt

- Streaming: Real-time reasoning trace via Streamlit callbacks

## ✨ Features

1. Natural language → SQL conversion

2. Supports SQLite and MySQL

3. Read-only database access

4. Prevents destructive queries

5. Real-time reasoning stream

6. Session-based chat history

7. Fast inference using Groq

8. Streamlit UI for rapid interaction

## 🔐 Safety Controls

The agent is explicitly restricted from executing:

- DELETE

- UPDATE

- INSERT

- DROP

All queries are read-only.

SQLite connections are opened in read-only mode.

This prevents accidental database corruption when using LLM agents.

## 🛠️ Tech Stack

    Python

    Streamlit

    LangChain

    Groq LLM API

    SQLAlchemy

    SQLite

    MySQL

## 📂 Project Structure
```bash
├── app.py
├── student.db
├── requirements.txt
└── README.md
```

## ⚙️ Installation
### 1. Clone repo
```bash
git clone https://github.com/yourusername/chat-with-sql-llm
```
    cd chat-with-sql-llm

### 2. Create environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
    pip install -r requirements.txt

## 🔑 Setup

### Get Groq API key:
https://console.groq.com/

### Run app:

    streamlit run app.py


Enter API key in sidebar.

## 🗄️ Supported Databases
- SQLite (default)

- Uses local student.db.

- MySQL

- Provide:

- host

- username

- password

- database name

## 💬 Example Queries

“Show all students with marks above 80”

“How many students are in each department?”

“List top 5 performers”

“Average score per subject”

## ⚠️ Limitations

No role-based access control

Prompt-level safety (not SQL sandboxing)

Not optimized for large schemas

No caching layer

No query cost monitoring

🔮 Future Improvements

Query validator layer

SQL sandboxing

role-based permissions

schema summarization

vector memory

query caching

multi-DB support

Docker deployment

latency benchmarking

## 🧪 Potential Extensions

Slack bot for data queries

BI dashboard integration

voice interface

analytics copilots

enterprise data assistant

## 👨‍💻 Author

Sahib Taj Singh \
AI/ML Engineer focused on practical LLM systems, computer vision, and ML infrastructure.