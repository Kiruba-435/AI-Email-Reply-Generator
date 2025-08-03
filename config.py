import os 
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
api_key = st.secrets["OPENROUTER_API_KEY"]
st.write("Loaded API Key:", api_key)
OPENROUTER_API_URL = "https://api.openrouter.ai/v1/chat/completions"


'''from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)'''