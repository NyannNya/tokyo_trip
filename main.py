# main.py
import streamlit as st
from components.sidebar import display_sidebar
from components.itinerary_display import display_itinerary
from data.itinerary_data import itinerary

# 設定頁面
st.set_page_config(page_title="東京 ~ 茨城 6日行程", page_icon="✈️", layout="wide")

# 取得可選擇的日期
dates = list(itinerary.keys())

# 顯示側邊欄並取得選定日期
selected_date = display_sidebar(dates[0], dates)

# 顯示行程
display_itinerary(selected_date.strftime("%Y-%m-%d")
)
