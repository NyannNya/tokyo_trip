# image_display.py
import streamlit as st
from PIL import Image
import os

def display_images(image_folder):
    image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    cols = st.columns(len(image_files))
    for col, img_path in zip(cols, image_files):
        image = Image.open(img_path)
        col.image(image, use_column_width=True)
