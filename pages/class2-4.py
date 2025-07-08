import streamlit as st

# st.number_input()可以輸入數字
# step=1可以讓使用者只能輸入整數
# min_value=0可以設定最小值為0
# max_value=100可以設定最大值為100
number = st.number_input("請輸入一個數字：", step=1, min_value=0, max_value=100)
# 顯示使用者輸入的數字
st.write(f"你輸入的數字是:{number}")
st.write("---")

st.write("##練習")
score = st.number_input("請輸入你的成績：", step=1, min_value=0, max_value=100)
if score >= 90:
    st.write("你的成績是A")
elif score >= 80:
    st.write("你的成績是B")
elif score >= 70:
    st.write("你的成績是C")
elif score >= 60:
    st.write("你的成績是D")
else:
    st.write("你的成績是F")
