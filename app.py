import streamlit as st
import google.generativeai as genai

# টাইটেল এবং ডিজাইন
st.set_page_config(page_title="K-AI SUPREME", layout="centered")
st.title("🤖 K-AI SUPREME")
st.caption("সৃষ্টি ও নির্দেশনায়: খোরশেদ আলম স্যার")

# Secrets থেকে API Key নেওয়া
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("এপিআই কি (API Key) সেটিংস এ কোনো সমস্যা হয়েছে। দয়া করে Secrets চেক করুন।")

# চ্যাট হিস্ট্রি শুরু করা
if "messages" not in st.session_state:
    st.session_state.messages = []

# আগের মেসেজগুলো দেখানো
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ইউজার ইনপুট
if prompt := st.chat_input("স্যার, আমি আপনার জন্য কী করতে পারি?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # এআই রেসপন্স
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"দুঃখিত খোরশেদ আলম স্যার, একটি সমস্যা হয়েছে: {str(e)}")
            
