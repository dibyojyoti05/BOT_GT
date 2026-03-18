
from dotenv import load_dotenv 
load_dotenv() 
import streamlit as st 
import os 
import google.generativeai as genai 
genai.configure(api_key=os.getenv("api_key"))
model = genai.GenerativeModel("gemini-2.5-flash") 

def my_output(query):
    response = model.generate_content(query) 
    return response.text 

#### UI Development using streamlit 

st.set_page_config(page_title="BOT_BHAI")
st.header("Hello Dibyojyoti, I am your BOT_BHAI....")
input = st.chat_input("Ask Your Question:" , key = "input")  
#submit = st.button("SUBMIT") 
#=================================================================
if input :
    with st.chat_message(input,avatar="🧑"):
        st.markdown(f"**{input}**")
    response = my_output(input) 
    st.subheader("Answer:")
    st.write(response)