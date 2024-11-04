# price_data.py
from .utils.BudgetCalculator import budget_calculator

# 定義價格資料，這裡可以根據需求載入不同的資料
price_tw = {
    "機票": 37158,
    "飯店": 13931 + 2698,
    "網路": 420,
    "保險": 4431,
}

price_jp = {
    "交通": 
        # day1 :
        # 機場 - 飯店, 飯店 - 上野, 上野 - 淺草, 押上 - 飯店
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
        330 + 680,
    "票券":
        # day1 : 上野動物園, 東京博物館, 墨田水族館, 晴空塔+天空迴廊
        600 + 1000 + 2500 + 3100 +
        # day2 : 雕刻森林美術館
        1800 +
        # day3 : 三鷹之森吉卜力美術館
        1000 +
        # day5 : 霞浦湖遊覽船, 偕樂園
        1570 + 300,
}

# 設定參數
num_people = 3  # 人數
exchange_rate = 0.21  # 匯率
fixed_costs = {
    "餐費": 1500 * 6, 
    "購物": 10000
    }  # 預估費用

# create_info
create_info = budget_calculator(
    domestic_costs= price_tw, 
    foreign_costs= price_jp, 
    fixed_costs= fixed_costs, 
    num_people=num_people, 
    exchange_rate=exchange_rate
    )

budget_table = create_info.generate_budget_table()
total_text = create_info.generate_total_text()