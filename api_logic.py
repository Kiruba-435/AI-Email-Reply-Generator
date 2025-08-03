from openai import OpenAI
from config import api_key

def query_openrouter_api(prompt, referer="https://ai-email-reply-generator.streamlit.app/", title="AI Email Replier"):
    try:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )
        extra_headers = {}
        if referer:
            extra_headers["HTTP-Referer"] = referer
        if title:
            extra_headers["X-Title"] = title
        completion = client.chat.completions.create(
            extra_headers=extra_headers,
            extra_body={},
            model="deepseek/deepseek-r1:free",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f'x some thing went wrong: {e}'