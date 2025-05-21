from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.llms import OpenAI
import streamlit as st

st.title("Ilham's Chat Bot")
input_txt = st.text_input("Please enter your queries here...")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is Ilham's assistant."),
    ("user", "{query}")
])

llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0) 
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_txt:
    response = chain.invoke({"query": input_txt})
    st.write(response)
