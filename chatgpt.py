from apikey import apikey
import os
import sys

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPEN_AI_KEY"] = apikey

query = sys.argv[1]
print(query)