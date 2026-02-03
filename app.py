import streamlit as st
import google.generativeai as genai

# ১. ইন্টারফেস সেটআপ
st.set_page_config(page_title="K-AI SUPREME", page_icon="⚡", layout="centered")
st.title("⚡ K-AI SUPREME")
st.caption("সৃষ্টি ও নির্দেশনায়: খোরশেদ আলম স্যার")

# ২. এপিআই কানেকশন (সবচেয়ে গুরুত্বপূর্ণ অংশ)
try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
        # এখানে 'gemini-1.5-flash' ব্যবহার করা হয়েছে যা আপনার আগের এররটি সমাধান করবে
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.warning("স্যার, আপনার এপিআই কি (API Key) এখনো সেটিংস-এ বসানো হয়নি।")
except Exception as e:
    st.error(f"দুঃখিত স্যার, কানেকশনে সমস্যা: {str(e)}")

# ৩. স্মার্ট মেমোরি ও চ্যাট
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("খোরশেদ আলম স্যার, আমি আপনার জন্য কী করতে পারি?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # সিস্টেম ইনস্ট্রাকশন সরাসরি এখানে দেওয়া হয়েছে
            full_prompt = f"You are K-AI, a powerful AI created by Khorshed Alam. Answer this: {prompt}"
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("স্যার, দয়া করে আপনার API Key-টি একবার চেক করুন।")
            
