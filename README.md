# LangChain Using Ollama & OpenAI

## Overview

This repository contains hands-on projects built while learning the LangChain ecosystem. It demonstrates how to build AI-powered applications using both cloud-based and local LLMs.

### Features

* Streamlit-based chatbot applications
* OpenAI integration using ChatOpenAI
* Local LLM integration using Ollama (Llama models)
* FastAPI and LangServe API development
* Prompt engineering with ChatPromptTemplate
* Output parsing with StrOutputParser
* LangSmith tracing and monitoring
* RAG (Retrieval-Augmented Generation) pipeline implementation

## Tech Stack

* LangChain Core
* LangChain OpenAI
* LangChain Ollama
* LangChain Community
* LangServe
* Streamlit
* FastAPI
* ChromaDB
* OpenAI Embeddings

## RAG Pipeline

```text
PDF / DOCX / Website
        ↓
      Loader
        ↓
   Text Splitter
        ↓
      Chunks
        ↓
 OpenAI Embeddings
        ↓
      Vectors
        ↓
     ChromaDB
        ↓
 Similarity Search
        ↓
        LLM
```

## Applications Built

* Streamlit Chatbot
* OpenAI-powered Chat Applications
* Ollama-powered Local LLM Applications
* FastAPI & LangServe APIs
* RAG-based Question Answering System

## Key Learnings

* Prompt Engineering
* LangChain Chains
* OpenAI & Ollama Integration
* Document Loaders
* Text Splitting
* Embeddings & Vector Databases
* ChromaDB Similarity Search
* FastAPI & LangServe
* LangSmith Tracing
* Building Production-Ready GenAI Applications
