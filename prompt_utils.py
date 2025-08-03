def build_custom_prompt(email, tone,intent):
    return f"""You are an assistant replying to an email. Respond in a {tone} tone.

Email received:
{email}


Your response should be focused on {intent}.
your reply:"""
