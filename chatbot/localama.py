from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import os 
import streamlit as st

from dotenv import load_dotenv

load_dotenv()

#provisding the keys
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

#prompttemplate kudukrathu
prompt= ChatPromptTemplate.from_messages([
    ("system","You are a helful assistant"),
    ("user","Question:{question}")
])

#ui loaadpannaum
st.title("welcome,its a chatbot app via using lagchain and langsmith")
input_text = st.text_input("Enter your questions")

llm = OllamaLLM(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm| output_parser

if input_text:
    response = chain.invoke({"question" : input_text})
    st.write(response)