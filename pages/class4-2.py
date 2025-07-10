import streamlit as st

# 初始化訂單列表
if "訂單" not in st.session_state:
    st.session_state.訂單 = []

# 標題
st.title("點餐系統")

# 設置一個兩欄佈局來對齊輸入框和加入按鈕
col1, col2 = st.columns([4, 1])

with col1:
    # 用戶手動輸入餐點名稱
    餐點 = st.text_input("請輸入餐點名稱:")

with col2:
    # 當按下加入按鈕時，將餐點加入訂單
    if st.button("加入餐點"):
        if 餐點:
            st.session_state.訂單.append(餐點)
            st.success(f"已加入: {餐點}")
        else:
            st.warning("請輸入餐點名稱")

# 設置右邊的操作區域
col1, col2 = st.columns([3, 1])

with col1:
    # 顯示當前已選的餐點
    if len(st.session_state.訂單) > 0:
        for i in range(len(st.session_state.訂單)):
            # 創建兩個列，一個顯示餐點名稱，另一個顯示刪除按鈕
            col1, col2 = st.columns([4, 1])  # 調整兩個欄位的寬度比例
            with col1:
                st.write(f"{i + 1}. {st.session_state.訂單[i]}")
            with col2:
                if st.button(f"刪除", key=f"remove_{i}"):
                    st.session_state.訂單.pop(i)
        st.write("目前沒有餐點，請加入餐點")
