import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load .env variables

def query_openrouter_api(prompt, referer=None, title=None):
    headers = {}
    if referer:
        headers["HTTP-Referer"] = referer
    if title:
        headers["X-Title"] = title

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Check your .env file or environment variables.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        default_headers=headers
    )

    completion = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct:free",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content
