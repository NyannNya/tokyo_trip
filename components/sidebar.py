# sidebar.py
import streamlit as st
from data import flight_data
from datetime import datetime

def display_sidebar(selected_date, dates):
    # 確保 dates 是 datetime 格式
    dates = [datetime.strptime(date, "%Y-%m-%d") if isinstance(date, str) else date for date in dates]
    
    st.sidebar.header("航班資訊")
    st.sidebar.subheader("去程")
    st.sidebar.write(f"""
    **出發**: {flight_data.departure_info["departure_time"]} - {flight_data.departure_info["from"]}  
    **到達**: {flight_data.departure_info["arrival_time"]} - {flight_data.departure_info["to"]}  
    **航班時間**: {flight_data.departure_info["duration"]}  
    """)
    
    st.sidebar.subheader("回程")
    st.sidebar.write(f"""
    **出發**: {flight_data.return_info["departure_time"]} - {flight_data.return_info["from"]}  
    **到達**: {flight_data.return_info["arrival_time"]} - {flight_data.return_info["to"]}  
    **航班時間**: {flight_data.return_info["duration"]}  
    """)
    
    # 日期範圍滑桿
    selected_date = st.sidebar.slider(
        "選擇日期以查看行程", 
        min_value=dates[0], 
        max_value=dates[-1], 
        value=dates[0]
    )
    
    # 預算估計
    price_tw = {
        "機票": 37158,
        "飯店": 13931 + 2698,
        "網路": 420,
        "保險": 4431,
    }
    price_jp = {
        "交通": 
            # day1 :
            # 機場 - 飯店, 飯店 - 上野, 上野 - 淺草, 押上 -飯店
            230 + 410 + 180 + 510 +
            # day2 :
            # 飯店 - 小原田 - 雕刻之森, 雕刻之森 - 大湧谷 - 桃源台, 桃源台 - 元箱根港, 元箱根港 - 橫濱, 橫濱 - 飯店
            1270 + 770 + 2090 + 1200 + 2330 + 280 +
            # day3 :
            # 飯店 - 吉祥寺, 吉祥寺 - 神樂坂, 神樂坂 - 秋葉原, 秋葉原 - 飯店
            640 + 320 + 150 + 410 +
            # day4 :
            # 飯店 - 東銀座, 築地市場 - 國立競技場, 新宿 - 原宿, 表參道 - 渋谷, 渋谷 - 東京車站 - 飯店
            410 + 220 + 150 + 180 + 210 + 410 +
            # day5 :
            # 飯店 - 飯店, 土浦 - 常磐神社入口, 水戸駅 - 大洗神社前, 大洗神社前 - 磯浜新道, 磯浜新道 - 飯店
            1570 + 1260 + 630 + 220 + 1590 +
            # day6 :
            # 飯店 - 石岡, 石岡 - 機場
            330 + 680
            ,
        "票券":
            # day1 : 上野動物園, 東京博物館, 墨田水族館, 晴空塔+天空迴廊
            600 + 1000 + 2500 + 3100 +
            # day2 : 雕刻森林美術館
            1800 +
            # day3 :三鷹之森吉卜力美術館
            1000 +
            # day5 : 霞浦湖遊覽船, 偕樂園
            1570 + 300
            ,
    }

    st.sidebar.markdown("---")
    st.sidebar.subheader("預算表")
    total_tw = sum(price_tw.values())
    total_jp = sum(price_jp.values())
    formatted_price = f"{(total_tw / 3 + round(total_jp * 0.21, 0)):,.0f}"

    # 預算項目表格
    budget_table = {
        "項目": [
            "機票", "飯店", "網路", "保險", "交通", "票券",
            "餐費", "購物"
               ],
        "金額": [
            "{:,}".format(int(price_tw["機票"] / 3)),
            "{:,}".format(int(price_tw["飯店"] / 3)),
            "{:,}".format(int(price_tw["網路"] / 3)),
            "{:,}".format(int(price_tw["保險"] / 3)),
            "{:,}".format(int(price_jp["交通"] * 0.21)),
            "{:,}".format(int(price_jp["票券"] * 0.21)),
            "{:,}".format(1500 * 6),
            "{:,}".format(10000)
        ]
    }
    st.sidebar.table(budget_table)
    st.sidebar.write(f"{formatted_price} + 19,000 ≒ 45,000 / 1人")
    
    return selected_date
