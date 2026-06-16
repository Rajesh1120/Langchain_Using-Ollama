# Langchain_Using-Ollama
# LangChain Learning Project

## Overview

This repository contains hands-on projects built while learning the LangChain ecosystem. The project demonstrates how to build AI-powered applications using both cloud-based and local Large Language Models (LLMs).

The repository includes:

* Chat applications built with Streamlit
* OpenAI integration using ChatOpenAI
* Local LLM integration using Ollama (Llama models)
* FastAPI-based API services
* LangServe for exposing LangChain chains as REST APIs
* Prompt engineering using ChatPromptTemplate
* Output parsing using StrOutputParser
* LangSmith tracing for monitoring and debugging LangChain applications

---

## Technologies Used

### LangChain Components

* ChatPromptTemplate
* StrOutputParser
* LangChain Core
* LangChain OpenAI
* LangChain Ollama
* LangChain Community
* LangServe

### LLM Providers

#### OpenAI

Used ChatOpenAI for production-ready cloud-based LLM applications.

#### Ollama

Used Ollama to run local open-source models such as Llama 2/Llama 3 without relying on external APIs.

---

## Applications Built

### 1. Streamlit Chat Application

A simple chatbot interface built using Streamlit.

Features:

* User input through a web UI
* Prompt templating
* LLM response generation
* Output parsing and display

### 2. OpenAI Integration

Implemented LangChain chains using:

* ChatOpenAI
* Prompt Templates
* Output Parsers

Used for cloud-hosted AI interactions.

### 3. Ollama Integration

Implemented local AI applications using:

* Ollama
* Llama models
* LangChain integration

Benefits:

* No OpenAI cost
* Local execution
* Privacy-focused development

### 4. FastAPI and LangServe APIs

Built API endpoints using FastAPI and LangServe.

Features:

* Exposed LangChain chains as REST APIs
* Added routes using add_routes()
* Generated OpenAPI documentation automatically
* Enabled integration with external applications

---

## Key Concepts Practiced

* Prompt Engineering
* Chain Creation
* LLM Integration
* Output Parsing
* Environment Variable Management
* API Development
* Local Model Deployment
* LangSmith Tracing
* FastAPI Routing
* OpenAPI Documentation

---

## Project Structure

* Streamlit applications
* FastAPI services
* LangServe APIs
* OpenAI-based chains
* Ollama-based chains
* Prompt templates
* Output parsers

---

## Learning Outcome

This project helped me understand:

1. How LangChain chains are created.
2. How prompts are managed using ChatPromptTemplate.
3. How to connect OpenAI and local Ollama models.
4. How to build Streamlit-based AI applications.
5. How to expose LangChain applications through FastAPI and LangServe.
6. How to monitor and debug applications using LangSmith tracing.
7. How to build the foundation for production-ready GenAI applications.

