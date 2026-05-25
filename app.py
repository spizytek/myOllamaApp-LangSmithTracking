import os
import dotenv
import streamlit as st
# from click import prompt

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Load environment variables from .env file
dotenv.load_dotenv() 
# for LangSmith tracking
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGCHAIN_PROJECT" )
os.environ["USER_AGENT"] = "true"

def streamlit_init():
    # Init streamlit app
    st.title("Ollama app with langsmith tracking")

def streamlit_input():
    # Get user input
    input_text = st.text_input("Enter your question here!")
    return input_text

def chatprompt_init():
    # Prompt template for the chatbot
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that provides concised information about the questions asked."),
        ("human", "Question: {input}")
    ])
    return prompt



def main():
    streamlit_init()
    input_text = streamlit_input()
    prompt = chatprompt_init()

    # Initialize the Ollama LLM
    llm = OllamaLLM(model="llama3.2")
    parser = StrOutputParser()

    # Create a chain that combines the prompt and the LLM
    chain = prompt|llm|parser

    if input_text:
        response = chain.invoke({"input": input_text})
        st.write(response)


if __name__ == "__main__":
    main()