import os
import dotenv

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser
import streamlit as st




dotenv.load_dotenv() # Load environment variables from .env file


# for LangSmith tracking
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGCHAIN_PROJECT" )
os.environ["USER_AGENT"] = "true"

# Init stramlit app
st.title("Ollama app with langsmith tracking")
input_text = st.text_input("Enter your question here!")


# Prompt template for the chatbot
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that provides concised information about the questions asked."),
    ("human", "Question: {input}")
])


# Initialize the Ollama LLM
llm = OllamaLLM(model="llama3.2")
parser = StrOutputParser()


chain = prompt|llm|parser

if input_text:
    response = chain.invoke({"input": input_text})
    st.write(response)


