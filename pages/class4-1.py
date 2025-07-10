import streamlit as st

st.title("欄位元件")
col1, col2= st.columns(2)#兩個欄位
col1.button("按鈕1",key="1")#在col1中建立一個類似st.button("按鈕1")
col2.button("按鈕2",key="2")#在col2中建立一個類似st.button("按鈕2")

#2columns,可以用比例來設定column的寬度,將比例放到list中
col1, col2= st.columns([1,2])
col3.button("按鈕3",key="3")
col3.button("按鈕4",key="4")

#3columns
col1, col2, col3 = st.columns([1,2,3])
col1.button("按鈕5",key="5")
col2.button("按鈕6",key="6")
col3.button("按鈕7",key="7")
st.write("---")#分隔線

col1,col2= st.columns([1,2])
with col1:
    st.write("col1")
    if st.button("按鈕8",key="8"):
        st.balloons()
with col2:
    st.write("col2")
    st.button("按鈕9",key="9")

#多個columns
cols = st.columns(4)
for i in range(len(cols)):
    with cols[i]:
        st.button(f"for當中的按鈕{i+1}",key=f"{i+10}")

st.write("---")
st.title("columns排列元件效果比較")
#只開一個row,兩個columns
col1, col2 = st.columns(2)
with col1:
    st.button("按鈕1",key="btn10")
    st.button("按鈕2",key="btn11")
    st.button("按鈕3",key="btn12")
with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")
st.write("---")
#3個row,2個columns
for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}",key=f"排版測試{i+4}")
    with col2:
        st.write(f"這是col2_{i+1}")

st.write("---")
st.title("文字輸入元件")
#st.text_input指令格式
text = st.text_input("請輸入文字",key="這是預設文字")
st.write(f"您輸入的文字是{text}")


st.title("session_state")
ans=1#設定一個變數ans=1
if st.button("按下去ans+1",key="ans"):
    ans=ans+1#ans+1
st.write(f"ans={ans}")


#session_state
if"ans1"not in st.session_state:#如果session_state中沒有ans這個變數
    st.session_stateans1=1#設定session_state.ans=1

if st.button("按下去ans+1",key="ans2"):
    st.session_state_ans1=st.session_state.ans+1
st.write(f"ans={st.session_state.ans1}")#顯示session_state.ans的值

#有時按鈕按下,不一定嘿重整畫面
#這時可使用st.return()強制重整畫面
if st.button("重新整理畫面",key="banana"):
    st.rerun()