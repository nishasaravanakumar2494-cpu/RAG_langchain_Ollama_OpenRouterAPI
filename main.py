#step 1 integrateing our code with open ai api try to create a search bar and itegrate wt open ai api
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from constants import openai_key

#integrating streamlit framework with open ai api
st.title("Langchain demo with open ai api")
input_text= st.text_input("Search the topic u want")

#integrating open ai api
llm = ChatOpenAI(
    api_key=openai_key,
    base_url="https://openrouter.ai/api/v1",
    model="mistralai/mistral-7b-instruct",
    temperature=0.7
)




if input_text:
    response = llm.invoke(input_text)
    st.write(response.content)
