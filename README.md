# Ollama Chatbot with LangSmith Tracking

A simple chatbot application built with **Streamlit**, **LangChain**, and **Ollama**. The application accepts user input, sends it to a local Llama 3.2 model via Ollama, and displays the generated response. LangSmith is integrated for tracing and monitoring LLM interactions.

## Features

* Streamlit-based web interface
* Local LLM inference using Ollama (Llama 3.2)
* LangChain prompt templating and chaining
* LangSmith observability and tracing

## Prerequisites

* Python 3.10+
* Ollama installed and running
* Llama 3.2 model downloaded
* LangSmith API key

## Installation

```bash
pip install streamlit python-dotenv langchain langchain-core langchain-ollama
ollama pull llama3.2
```

Create a `.env` file:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=ollama-chatbot
```

## Run

```bash
streamlit run app.py
```

## How It Works

1. User enters a question in the Streamlit UI.
2. LangChain formats the prompt.
3. Ollama processes the request using the Llama 3.2 model.
4. The response is parsed and displayed.
5. LangSmith logs the interaction for monitoring.

## Technologies

* Python
* Streamlit
* LangChain
* Ollama
* Llama 3.2
* LangSmith
