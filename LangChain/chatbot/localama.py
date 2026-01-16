from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama # 3rd party integration
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="false"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the queries"),
        ("user","Question:{question}")
    ]
)

# streamlit framework
st.title('Langchain Demo with LLAMA2 API')
input_text=st.text_input("Search the topic you want")

# ollama:llama3 LLM
llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))