import streamlit as st
import os
import time
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores import FAISS

load_dotenv()

groq_api_key = os.environ["GROQ_API_KEY"]

if "vectors" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="nomic-embed-text")
    st.session_state.loader = WebBaseLoader("https://docs.smith.langchain.com/")
    st.session_state.docs = st.session_state.loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documents = splitter.split_documents(
        st.session_state.docs[:50]
    )

    st.session_state.vectors = FAISS.from_documents(
        st.session_state.final_documents,
        st.session_state.embeddings
    )

st.title("Chat Groq RAG")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="gemma-7b-it"
)

prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based only on the context below.
    <context>
    {context}
    </context>
    Question: {input}
    """
)

document_chain = create_stuff_documents_chain(llm, prompt)
retriever = st.session_state.vectors.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

user_prompt = st.text_input("Input your prompt here")

if user_prompt:
    start = time.process_time()
    response = retrieval_chain.invoke({"input": user_prompt})
    st.write("Response time:", time.process_time() - start)

    st.write(response["answer"])

    with st.expander("Document Similarity Search"):
        for doc in response["context"]:
            st.write(doc.page_content)
            st.write("-----")
