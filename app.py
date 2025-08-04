# app.py
import streamlit as st
from prompt_utils import build_custom_prompt
from api_logic import query_openrouter_api 
from feedback_handler import save_feedback

'''st.secrets["OPENROUTER_API_KEY"]'''


st.set_page_config(page_title="📬 AI Email Replier", layout="centered")

# Add background image and light pink/blue colors using custom HTML/CSS
st.markdown("""
<style>
body {
  background-image: url('https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=1200&q=80');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
}
.main-title {
  text-align: center;
  font-size: 2.3em;
  font-weight: bold;
  color: #fff;
  background: linear-gradient(90deg, #fceabb 0%, #f8bfe7 100%);
  border-radius: 16px;
  padding: 18px 0 18px 0;
  margin-bottom: 18px;
  letter-spacing: 1px;
  box-shadow: 0 2px 12px #f8bfe780;
}
.feature-panel {
  background: linear-gradient(90deg, #f8bfe7 0%, #b5d8f6 100%);
  border-radius: 16px;
  padding: 18px;
  margin-bottom: 24px;
  box-shadow: 0 2px 8px #b5d8f640;
}
.input-panel {
  background: linear-gradient(90deg, #e0c3fc 0%, #b5d8f6 100%);
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: 0 2px 8px #b5d8f640;
}
.footer-panel {
  background: linear-gradient(90deg, #f8bfe7 0%, #b5d8f6 100%);
  border-radius: 16px;
  margin: 32px auto 0 auto;
  max-width: 700px;
  padding: 24px;
  box-shadow: 0 2px 12px #b5d8f640;
}
.footer-author {
  display: inline-block;
  background: linear-gradient(90deg, #f8bfe7, #b5d8f6);
  color: #333;
  font-size: 1.3em;
  font-weight: bold;
  padding: 12px 32px;
  border-radius: 32px;
  box-shadow: 0 2px 8px #b5d8f640;
}
h3, .stSubheader {
  color: #e75480 !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<div class='main-title'>📨 AI Powered Email Reply Generator</div>", unsafe_allow_html=True)

# Images for email features and use cases
st.markdown("""
<div class='feature-panel' style='display: flex; justify-content: center; gap: 32px;'>
  <div style='text-align: center;'>
    <img src='https://cdn-icons-png.flaticon.com/512/561/561127.png' width='80'>
    <p style='font-size: 1em; color: #fff; font-weight: bold;'>Automated Email Replies</p>
  </div>
  <div style='text-align: center;'>
    <img src='https://cdn-icons-png.flaticon.com/512/1077/1077012.png' width='80'>
    <p style='font-size: 1em; color: #fff; font-weight: bold;'>Personalized Responses</p>
  </div>
  <div style='text-align: center;'>
    <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='80'>
    <p style='font-size: 1em; color: #fff; font-weight: bold;'>Save Time & Boost Productivity</p>
  </div>
</div>
""", unsafe_allow_html=True)

# Input Panel
st.markdown("<div class='input-panel'>", unsafe_allow_html=True)
with st.form("email_reply_form"):
    st.subheader("Paste Received Email")
    email = st.text_area("Received Email", height=150)

    st.subheader("Choose Reply Style")
    tone = st.selectbox("Reply Style", ["polite", "casual", "assertive"])

    st.subheader("Describe Reply Intent")
    intent = st.text_input("Reply Intent (e.g., accept, decline, request info)")

    submitted = st.form_submit_button("Generate Reply")
st.markdown("</div>", unsafe_allow_html=True)

# Reply Generation & UI
if submitted:
    if email and intent:
        prompt = build_custom_prompt(email, tone, intent)
        reply = query_openrouter_api(prompt)

        st.subheader("✍️ Edit Your Reply")
        edited_reply = st.text_area("Refine your reply if needed", value=reply, height=200)

        # Feedback Panel
        st.subheader("📣 Feedback")
        col1, col2 = st.columns(2)
        like = col1.button("👍 Like")
        dislike = col2.button("👎 Dislike")
        comment = st.text_area("Additional Feedback (optional)")


        if like or dislike or comment:
            save_feedback(edited_reply, like, dislike, comment)
            st.success("✅ Feedback saved!")
    else:
        st.error("⚠️ Please complete all fields before generating your reply.")

# Footer (unique style with emojis and user-attracting description)
st.markdown("""
<hr>
<div class='footer-panel'>
  <h3 style='color: #ee0979;'>Why use this app?</h3>
  <p style='font-size: 1.1em; color: #333;'>
    ✉️ <b>Instantly generate professional email replies</b> tailored to your style and intent.<br>
    🤖 <b>Save time</b> and boost productivity with AI-powered suggestions.<br>
    🎯 <b>Personalize every response</b> for better communication.<br>
    🔒 <b>Keep your workflow simple</b> and efficient.<br>
    <br>
    <i>Perfect for busy professionals, customer support, and anyone who wants to reply smarter and faster!</i>
  </p>
</div>

<div style='text-align: center; margin-top: 36px;'>
  <span class='footer-author'>
    🚀 Crafted with ❤️ by <span style='color: #fff200; text-shadow: 1px 1px 2px #333;'>Kiruba</span> ✉️
    <a href='https://www.linkedin.com/in/mkiruba435' target='_blank' style='margin-left:18px; margin-right:8px; text-decoration:none;'>
      <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg' width='28' style='vertical-align:middle;'>
    </a>
    <a href='https://github.com/kiruba-435' target='_blank' style='margin-left:8px; text-decoration:none;'>
      <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg' width='28' style='vertical-align:middle;'>
    </a>
  </span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div>✉️ ...</div>
""", unsafe_allow_html=True)
