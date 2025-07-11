import streamlit as st
import os

st.title("圖片元件")
# st.image指令，參數(圖片檔案路徑，寬度)
st.image("image/下載.jpg", width=300)

image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

image_size = st.number_input("請輸入圖片大小", min_value=100, step=1, max_value=500)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=300)
    # 顯使圖片，根據使用者樹入的大小調整寬度

for image_file in image_files:
    # 除了width，還有use_container_width
    st.image(f"{image_folder}/{image_file}", use_container_width=image_size)

select_image = st.selectbox("請選擇圖片", image_files)
st.image(f"{image_folder}/{select_image}", width=300)
