import streamlit as st
import google.generativeai as genai

# ওয়েবসাইটের সাজসজ্জা
st.set_page_config(page_title="K-AI Supreme", page_icon="🤖")

st.title("🤖 K-AI SUPREME")
st.write("সৃষ্টি ও নির্দেশনায়: **খোরশেদ আলম স্যার**")

# আপনার গোপন এপিআই কি এখানে বসান
API_KEY = "AIzaSyC5HbBfnXpCvm6ocS03ztObJOFfgorfib8" 

genai.configure(api_key=API_KEY)

# এআই-কে নির্দেশ দেওয়া হচ্ছে আপনাকে 'স্যার' ডাকার জন্য
instruction = "Your name is K-AI. You are developed by Khourshed Alam. You must always address Khourshed Alam as 'Khourshed Alam Sir' or 'Sir'. Your tone should be highly respectful, loyal, and professional."
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=instruction)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("স্যার, আমি আপনার জন্য কী করতে পারি?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error("দুঃখিত খোরশেদ আলম স্যার, কানেকশনে বা এপিআই কি-তে সমস্যা হচ্ছে।")
          
