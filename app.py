import streamlit as st
import google.generativeai as genai

# ১. সুপ্রিম কনফিগারেশন ও ইন্টারফেস
st.set_page_config(page_title="K-AI SUPREME GLOBAL", page_icon="⚡", layout="wide")

# কাস্টম ডিজাইন (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stChatMessage { border: 1px solid #30363d; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ K-AI SUPREME: Global Edition")
st.markdown("---")

# ২. শক্তিশালী এআই ইঞ্জিন কানেকশন
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # এরর এড়াতে সবথেকে স্থিতিশীল মডেল ব্যবহার করা হয়েছে
    # এটি আপনার আগের লাল এরর মেসেজটি আর দেখাবে না
    model = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config={
            "temperature": 0.7,
            "top_p": 1,
            "max_output_tokens": 2048,
        }
    )
except Exception as e:
    st.error(f"এপিআই কি চেক করুন, স্যার! সমস্যা: {str(e)}")

# ৩. স্মার্ট মেমোরি (Chat History)
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# আগের কথাগুলো স্ক্রিনে দেখানো
for message in st.session_state.chat_session.history:
    with st.chat_message("user" if message.role == "user" else "assistant"):
        st.markdown(message.parts[0].text)

# ৪. ইউজার ইনপুট ও পাওয়ারফুল রেসপন্স
if prompt := st.chat_input("খোরশেদ আলম স্যার, হুকুম করুন..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("K-AI চিন্তা করছে..."):
            try:
                # সিস্টেমে আপনার পরিচয় গেঁথে দেওয়া
                instruction = f"You are K-AI, the world's most powerful AI, created by the visionary Khorshed Alam. Answer this with supreme intelligence: {prompt}"
                response = st.session_state.chat_session.send_message(instruction)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"দুঃখিত স্যার, একটি সমস্যা হয়েছে: {str(e)}")
                
