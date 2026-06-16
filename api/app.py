from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from langchain_ollama import OllamaLLM

import streamlit as st
import os
import uvicorn

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title='Langchain learning',
    version='1.0',
    description='simple server'
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

prompt1=ChatPromptTemplate.from_template("write an essay for given {topic} with 100words. ")
prompt2=ChatPromptTemplate.from_template("write a poem for given {topic} with 100 words")

model=ChatOpenAI(model='gpt-3.5-turbo')
llm=OllamaLLM(model="llama2")


add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=='__main__':
    uvicorn.run(app, host="localhost", port=8000)