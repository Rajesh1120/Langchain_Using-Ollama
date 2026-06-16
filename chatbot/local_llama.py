from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt template
prompt= ChatPromptTemplate.from_messages([
    ('system', 'you are helpful assistant. Please respond for user queries'),
    ('user', 'Question: {question}')
])
## streamlit framework
st.title("Langchain demo with openai api")
input_text=st.text_input("Search the topic you want")

## llm model
llm=OllamaLLM(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))
