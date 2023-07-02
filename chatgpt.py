import os
import streamlit as st
import streamlit as streamlit

from apikey import apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Prompt templates
title_template = PromptTemplate(
    input_variables=["topic"],
    template="Who is the president of {topic}"
)

script_template = PromptTemplate(
    input_variables=["title"],
    template="Write me a short biography of the president of the following country: {title}"
)

os.environ["OPENAI_API_KEY"] = apikey

#App framework
st.title("🦜️🔗 LangChain Testing")
prompt = st.text_input("The place for your prompt is down below:")

# LLMs
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key="title")
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key="script")
sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=["topic"],
                                   output_variables=["title", "script"], verbose=True)

# Showing the answer to the prompt
if prompt:
    response = sequential_chain.run(prompt, return_only_outputs=True)
    st.write(response)

