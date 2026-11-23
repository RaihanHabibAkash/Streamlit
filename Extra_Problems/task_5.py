# Task 5: Gemini Chatbot App
from google import genai 
import os 
from dotenv import load_dotenv
import streamlit as st

load_dotenv() # env ar sob variable paisi
api_key = os.environ.get("API_KEY")
client = genai.Client(api_key=api_key)

txt = st.text_input("What is you Qus?")
pressed = st.button("Ask Gemini",type="primary")

if pressed :
    if txt :
        response = client.models.generate_content(
            model = "gemini-3.8-flash",
            contents=txt
        )
        st.markdown(response.text)
    else :
        st.warning("Enter text first")
# Got a error need to solve