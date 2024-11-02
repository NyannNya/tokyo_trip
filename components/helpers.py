# helpers.py
import os
from PIL import Image
import streamlit as st

def display_images_from_folder(image_folder):
    image_folder = os.path.join("image", image_folder)
    if os.path.isdir(image_folder):  # 檢查資料夾是否存在
        image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith(('.png', '.jpg', '.jpeg'))]
        cols = st.columns(len(image_files))  # 根據圖片數量設置列數           
        for col, img_path in zip(cols, image_files):
            image = Image.open(img_path)
            col.image(image, width=400)  # 顯示圖片
    else:
        st.write("圖片資料夾不存在或路徑錯誤")
