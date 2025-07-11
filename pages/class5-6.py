import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# 初始化歷史紀錄
if "history" not in st.session_state:
    st.session_state.history = []

if "system_message" not in st.session_state:
    st.session_state.system_message = "請用繁體中文進行後續對話"

# 設置三個布局
col1, col2 = st.columns([6, 1])
with col1:
    st.session_state.system_message = st.text_input(
        " 系統訊息", st.session_state.system_message
    )


with col2:
    if st.button("😊"):
        st.session_state.history = []
        st.rerun()


for message in st.session_state.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])

prompt = st.chat_input("請輸入你的訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model="gpt-4o-mini-search-preview",
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.history,
    )

    assiant_massage = response.choices[0].message.content
    st.session_state.history.append({"role": "assistant", "content": assiant_massage})
    # 將ai駐守的訊息加入對話紀錄
    st.rerun()
