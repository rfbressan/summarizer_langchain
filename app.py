# Streamlit app to use LangChain

import os
from dotenv import load_dotenv

from langchain.llms import OpenAI

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.2)

llm.predict(
    "What would be a good company name for a company that makes colorful socks?"
)
