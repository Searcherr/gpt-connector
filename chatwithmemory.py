"""Python file to serve as the frontend"""
import streamlit as st
from streamlit_chat import message
import os

from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from apikey import apikey
from langchain.retrievers import TFIDFRetriever
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain import PromptTemplate

os.environ["OPENAI_API_KEY"] = apikey

retriever = TFIDFRetriever.from_texts(
    ["Our client, a gentleman named Jason, has a dog whose name is Dobby",
     "Jason has a good friend called Emma",
     "Emma has a cat whose name is Sullivan"])

template = """
Use the following context (delimited by <ctx></ctx>) and the chat history (delimited by <hs></hs>) to answer the question:
------
<ctx>
{context}
</ctx>
------
<hs>
{history}
</hs>
------
{question}
Answer:
"""

prompt = PromptTemplate(
    input_variables=["history", "context", "question"],
    template=template,
)

def load_chain():
    """Logic for loading the chain you want to use should go here."""
    llm = OpenAI(temperature=0)
    chain = ConversationChain(llm=llm)
    return chain

chain = load_chain()

# From here down is all the StreamLit UI.
st.set_page_config(page_title="C️🔗 LangChain Testing", page_icon=":bird:")
st.header("Let's test the LangChain")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


def get_text():
    input_text = st.text_input("You: ")
    return input_text


user_input = get_text()

if user_input:
    output = chain.run(input=user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")