import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://api.openrouter.ai/v1/chat/completions"


'''from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)'''