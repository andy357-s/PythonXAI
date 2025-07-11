import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是AI的訊息")

# 對話
history = [
    {"role": "system", "content": "請用繁體中文進行後續對話"},
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "很開心認識你"},
]

for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
