import streamlit as st

st.write("### 按鈕練習")
# st.button()可以顯示一個按鈕，使用者可以點擊他
# key可以設定按鈕的名稱，可以用來區分不同按鈕
# 如果使用者點及按鈕，st.button()會傳回True，否則回傳False
st.button("按我一下", key="btn1")
if st.button("按我一下", key="btn2"):
    st.balloons()
if st.button("按我一下", key="btn3"):
    st.snow()

st.title("### 數字金字塔")
number = st.number_input("請輸入一個數字：", step=1, min_value=1, max_value=9)
for i in range(1, number + 1):
    st.write(f"{i}" * i)
