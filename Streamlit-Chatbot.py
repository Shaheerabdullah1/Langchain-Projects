# Q&A Chatbot
from dotenv import load_dotenv
import streamlit as st
import os
from langchain.llms import OpenAI



# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")


# Func to get the response for the Query.
def get_openai_response(question):
    llm = OpenAI(api_key=openai_api_key, temperature=0.6)
    response=llm(question)
    return response
    

# initialize the stramlit application
st.set_page_config(page_title="Q&A Chatbot",page_icon='🤖')

st.header("LangChain-Application")
input = st.text_input('Input:',key=input)

response=get_openai_response(input)

submit=st.button('Generate')

if submit:
    st.subheader('The Response is')
    st.write(response)




















