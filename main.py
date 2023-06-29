import os
import streamlit as st
import streamlit as streamlit

from apikey import apikey
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = apikey

#App framework
st.title("🦜️🔗 LangChain Testing")
prompt = st.text_input("The place for your prompt is down below:")

# LLMs
llm = OpenAI(temperature=0.9)

# Showing the answer to the prompt
if prompt:
    response = llm(prompt)
    st.write(response)
