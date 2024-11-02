# itinerary_data.py

# 必填: attraction, start_time, end_time, description, 
# 選填: duration=None, meal_time=None, transport=None, return_time=None

itinerary = {
    "2024-12-13": {
        "title": "開啟日本之旅的序幕：從台北出發前的準備到羽田機場",
        "start": {
            "attraction": "台北桃園機場",
            "start_time": "21:00",
            "end_time": "04:00",
            "duration": "7 小時",
            "transport": "交通：➡➡ 機場",
            "description": 
                "⚠️ 重要訊息 \n\n" +
                "➖ 請務必準時抵達機場於班機起飛前2.5小時開始辦理櫃台報到及行李託運手續，請旅客務必於起飛前 45 分鐘完成報到\n\n" +
                "➖ 航班時間: 00:10，請於 21:00 開始進行報到。\n\n" +
                "🌥️ 天氣預報 \n\n"+
                "➖ https://www.japan.travel/tw/weather/kanto/tokyo/ \n\n" +
                "📶 WIFI \n\n"+
                "➖ 取件地點: JETFI台北門市 (捷運南京三民: 105台北市松山區南京東路五段92號3樓) \n\n" +
                "➖ 取件時間: 12-13 (五) 09:00-18:00",
            "file": "image\\day0_airport"
        },
    },
    "2024-12-14": {
        "title": "東京文化盛宴：上野至淺草的歷史與現代交錯之旅",
        "start": {
            "attraction": "クインテッサホテル東京羽田",
            "alias": "東京羽田 QUINTESSA",
            "start_time": "04:00",
            "end_time": "08:00",
            "duration": "4 小時",
            "transport": "交通：出境 ➖ 羽田機場 京急機場線 6分鐘 ➡➡ 糀谷站",
            "description": 
                "飯店的特色之一是設有名為「MANGA Library」的漫畫圖書館，收藏約8,000冊漫畫，供住客免費閱讀。\n\n" +
                "此外，飯店提供24小時的免費飲料吧，以及咖哩和烏龍麵等輕食服務，讓住客在任何時間都能享用。\n\n" +
                "預計住宿: 12-14 - 12-18，4晚",
            "file": "image\\day1_hotel"
        },
        "morning":{
            "attraction": "上野公園",
            "start_time": "08:00",
            "end_time": "14:00",
            "duration": "6 小時",
            "transport": "交通：飯店 ➖ 京急蒲田 9分鐘 ➖ (轉車) 品川 JY山手線 22分鐘 ➡➡ 鶯谷",
            "description": 
                "行程: 東京博物館 ➡➡ 上野動物園 ➡➡ 五條天神社 ➡➡ 不忍池 ➡➡ 阿美橫丁\n\n"+  
                "購票: \n\n" +
                    "➖ 上野動物園: https://www.asoview.com/channel/ticket/5ciQtROJoA/ticket0000028208 \n\n" +
                "景點: \n\n" +
                    "➖ 東京博物館: https://www.tnm.jp/modules/r_free_page/index.php?id=1659&lang=en \n\n" +
                    "➖ 國立科學博物館: https://www.tnm.jp/modules/r_free_page/index.php?id=1659&lang=en \n\n" +
                    "➖ 東京都美術館: https://www.tobikan.jp/tw/exhibition/index.html \n\n" +
                    "➖ 東京西洋美術館: https://www.nmwa.go.jp/zh/ \n\n" +
                "美食: \n\n" +
                    "➖ 肉の大山: 創立於1932年的肉類批發直營店，以炸牛肉餅和可樂餅聞名。\n\n" +
                    "➖ 西湖春上海小籠包: 烤小籠包的店。烤小籠包外皮酥脆，內餡湯汁滾燙，適合邊走邊吃。\n\n" +
                    "➖ 茶の君野園: 日本茶專賣店，以抹茶霜淇淋廣受歡迎。\n\n" +
                    "➖ 志村商店: 知名的巧克力叫賣商店。\n\n" +
                "路線: https://myppt.cc/7zsOxT",
            "file": "image\\day1_morning"
        },
        "afternoon":{
            "attraction": "淺草",
            "start_time": "14:00",
            "end_time": "18:00",
            "duration": "4 小時",
            "transport": "交通：上野 ➖ 上野廣小路 銀座線 7分鐘 ➡➡ 淺草 ➡➡ 仲見世通 ➡➡ 淺草寺 ➡➡ 五重塔 ➡➡ 淺草西參道 ➡➡ 淺草文化觀光中心",
            "description": 
                "景點: \n\n" +
                    "➖ 淺草寺: 「雷門」，「寶藏門」、「五重塔」、「本堂」\n\n" +
                    "➖ 淺草西參道: 江戶風情拱廊及木頭步道\n\n" +
                    "➖ 淺草花屋敷: 日本最古老的遊樂園\n\n" +
                    "➖ 淺草文化觀光中心: 免費看風景的展望台\n\n" +
                "美食: \n\n" +
                    "➖ 仲見世通: \n\n" +
                        "➖➖ 淺草九重: 炸饅頭、\n\n" +
                        "➖➖ 淺草吉備糰子 AZUMA: 吉備糰子\n\n" +
                        "➖➖ 淺草燈籠最中: 糯米紅豆湯\n\n" +
                        "➖➖ 木村家本店: 雞蛋糕\n\n" +
                    "➖ 西參道商店街: \n\n" +
                        "➖➖ 花月堂: 波羅麵包\n\n",
            "file": "image\\day1_afternoon"
        },
        "evening":{
            "attraction": "押上",
            "start_time": "18:00",
            "end_time": "22:00",
            "duration": "4 小時",
            "transport": "交通：隅田公園 ➖ 隅田川步道橋 ➡➡ 東京水岸街道 ➡➡ 墨田水族館 ➡➡ 東京晴空街道 ➡➡ 晴空塔",
            "description": 
                "景點: \n\n" +
                    "➖ 東京水岸街道: 東京水岸街道位於隅田公園和東京晴空塔之間。沿著「隅田川步道橋」散步6 分鐘過橋，從商場「西區」往東區逛。\n\n" +
                    "➖ 墨田水族館: 主打為企鵝、水母、金魚、花園鰻\n\n" +
                    "➖ 東京晴空街道: https://www.tokyo-skytree.jp/en/ \n\n" +
                    "➖ 東京晴空塔: 東京晴空塔高塔高634公尺，被金氏世界紀錄認證為「世界第一高塔」\n\n" +
                    "➖ 夢幻聖誕: https://tokyo.letsgojp.com/archives/704199\n\n" +                    
                "美食: \n\n" +
                    "➖ 敘敘苑 晴空塔店: 高級燒肉餐廳\n\n" +
                    "➖ 六厘舍: 知名沾麵店，以濃郁的魚介豚骨湯頭聞名\n\n" +
                    "➖ 迴轉壽司 魚心: 主打大份壽司，手握壽司已是一般壽司的4倍大！\n\n" +
                    "➖ 天丼 金子半之助: 日本全國丼金賞獎，以原汁原味演繹江戶時代的傳統風味，重金自日本引進江戶時代獨家秘傳醬汁，並採用日本進口胡麻油\n\n",
            "file": "image\\day1_evening"
        },
        "return":{
            "attraction": "返回飯店",
            "start_time": "22:00",
            "transport": "交通：押上 ➖ 押上 淺草線 + 京急本線 39分 ➡➡ 京急蒲田 ➡➡ 飯店"
        }
    },
    "2024-12-15": {
        "title": "箱根藝術與自然之旅：美術館、地熱奇觀與海盜船的獨特體驗",
        "start": {
            "attraction": "小原田站",
            "start_time": "08:00",
            "end_time": "09:30",
            "duration": "1.5 小時",
            "transport": "交通：飯店 ➖ 糀谷站 京急本線 12分 ➖ (轉車) 橫濱 東海道本線 52分 ➡➡ 小原田"
        },
        "morning": {
            "attraction": "箱根雕刻森林美術館",
            "start_time": "10:00",
            "end_time": "14:00",
            "duration": "4 小時",
            "transport": "交通：小原田 ➖ 箱根登山線 15分  ➖ (轉車) 箱根湯本 箱根登山線 36分  ➡➡ 雕刻之森 ➡➡ 箱根雕刻森林美術館",
            "description": 
                "景點: \n\n" +
                    "➖ 箱根雕刻森林美術館: 館內展示約120件近代與現代知名雕塑家的作品，包括羅丹、亨利·摩爾、米羅等藝術大師的傑作。" + 
                    "除了戶外雕塑，館內還設有「畢卡索館」，收藏超過300件畢卡索的作品，涵蓋繪畫、陶藝、雕刻等多種形式。此外，館內設有天然溫泉足湯，讓參觀者在欣賞藝術之餘，享受放鬆身心的體驗。\n\n",
            "file": "image\\day2_morning"
        },
        "afternoon_1": {
            "attraction": "大湧谷",
            "start_time": "14:00",
            "end_time": "15:30",
            "duration": "1.5 小時",
            "transport": "交通：雕刻之森 ➖ 箱根登山線 3分 ➖ (轉車) 強羅 ➖ 箱根登山纜車 11分 ➖ (轉車) 早雲山 ➖ 箱根空中纜車 10分 ➡➡ 大湧谷",
            "description": 
                "景點: \n\n" +
                    "➖ 大湧谷: 約3000年前火山爆發所形成的火山口遺跡。這裡至今仍不斷噴出硫磺蒸氣，形成獨特的地熱景觀，被稱為「地獄谷」\n\n" ,
            "file": "image\\day2_afternoon_1"
        },
        "afternoon_2": {
            "attraction": "箱根海盜船",
            "start_time": "15:30",
            "end_time": "16:30",
            "duration": "1 小時",
            "transport": "交通：大湧谷 ➖ 箱根空中纜車 30分 ➡➡ 桃源台 ➖ (轉船) 海賊船 桃源臺港 ➡➡ 箱根海賊船 元箱根港",
            "description": 
                "景點: \n\n" +
                    "➖ 箱根海盜船: 蘆之湖運航的觀光船，由於其觀光船均以17世紀至19世紀中期戰列艦為原型，故又以「箱根海賊觀光船」\n\n" ,
            "file": "image\\day2_afternoon_2"
        },
        "evening":{
            "attraction": "橫濱",
            "start_time": "16:30",
            "end_time": "22:30",
            "duration": "4 小時",
            "transport": 
                "交通：元箱根港 ➖ 元箱根港（バス）箱根町線：箱根口経由小田原駅行 57分 ➖ (轉車) 小田原 ➖ 東海道本線 50分 ➡➡ 橫濱\n\n "+ 
                    "➡➡ (轉車) 港未來線各站停車元町、中華街 13分 ➡➡ 元町、中華街 ➡➡ 山下公園 ➡➡ 橫濱紅磚倉庫 ➡➡ 橫濱",
            "description": 
                "購物: \n\n" +
                    "➖ 山下公園: 夜之橫濱燈光秀 https://yorunoyo.yokohama/\n\n" +                  
                    "➖ 橫濱紅磚倉庫 : 橫濱聖誕市集 \n\n" +
                    "➖ 橫濱PORTA: 前往其他購物商城如「Yokohama Sky Building」、「丸井CITY橫濱」、「SOGO橫濱店」時的中繼站\n\n" +
                    "➖ (20:30) LUMINE橫濱:集結各大年輕時尚品\n\n" +
                    "➖ (20:30) 丸井CITY橫濱: 流行服飾、雜貨等商品為主，還有「Pokémon Center」！\n\n" +
                    "➖ (20:00) SOGO橫濱店:設有LoFt、紀伊國屋書店、無印良品等\n\n" +
                    "➖ (22:00) BAY QUARTER YOKOHAMA: 「海港」風情的百貨商城\n\n",
            "file": "image\\day2_evening"           
        },
        "return": {
            "attraction": "返回飯店",
            "start_time": "22:30",
            "transport": "交通：橫濱 ➖ 京急本線 急行羽田機場 15分 ➡➡ 京急蒲田 ➡➡ 飯店"
        }
    },
    "2024-12-16": {
        "title": "",
        "morning_1": {
            "attraction": "築地市場",
            "start_time": "07:00",
            "end_time": "09:00",
            "duration": "2 小時",
            "transport": "交通：飯店 ➖ 京急蒲田 京急本線 ➖ 東銀座 ➡➡ 築地市場",
            "description": 
                "美食: \n\n" +
                    "➖ 築地虎杖海膽飯: 以新鮮海膽蓋飯聞名，特別是「五色海膽飯」\n\n" +
                    "➖ 狐狸屋牛丼: 以味噌燉煮的牛內臟蓋飯著稱，風味濃郁\n\n" +
                    "➖ 築地壽司清: 老字號壽司店，提供新鮮壽司\n\n" +
                    "➖ 丸武玉子燒: 口感綿密，甜度適中，是築地市場的經典小吃\n\n" +
                    "➖ 築地黑銀鮪魚屋: 以新鮮現切的鮪魚生魚片和壽司聞名\n\n",          
            "file": "image\\day3_morning_1"
        },
        "morning_2": {
            "attraction": "新宿御苑",
            "start_time": "09:00",
            "end_time": "13:00",
            "duration": "4 小時",
            "transport": "築地市場 大江戶線 大門/六本木方面 16分 ➡➡ 國立競技場 ➡➡ 新宿御苑 ➡➡ 花園神社 ➡➡ 思い出橫丁（回憶橫丁）",
            "description": 
                "景點: \n\n" +
                    "➖ 新宿御苑: 融合日式、英式和法式風格的大型庭園。\n\n" +
                    "➖ 花園神社: 在德川家康時期創建的鎮守神社，主要供奉日本神衹「倉稻魂命」、「日本武」和「受持神」\n\n" +
                    "➖ 回憶橫丁: 充滿昭和時代風情，擁有許多小型居酒屋和餐館，適合體驗日本傳統飲食文化。\n\n" + 
                "美食: \n\n" +
                    "➖ かめや: 蕎麥麵店以平價美味著稱，特別是「天玉そば」（炸蔬菜天婦羅加溫泉蛋蕎麥麵）\n\n" +
                    "➖ 岐阜屋: 這家中華料理店提供各式麵類、煎餃和炒飯，其中「豬肉木耳炒蛋」是必點菜色。\n\n" +
                    "➖ 鳥園: 以烤雞串聞名，提供多樣的串燒選擇。\n\n",
            "file": "image\\day3_morning_2"
        },
        "afternoon": {
            "attraction": "表參道",
            "start_time": "13:00",
            "end_time": "17:00",
            "duration": "4 小時",
            "transport": "交通：新宿 ➖  山手線各站停車品川 / 澀谷方面(內環線) 5分 ➡➡ 原宿 ➡➡ 明治神宮 ➡➡ 表參道",
            "description":
                "",
            "file": "image\\day3_afternoon"
        },
        "evening": {
            "attraction": "秋葉原",
            "start_time": "17:00",
            "end_time": "21:00",
            "duration": "4 小時",
            "transport": "交通：",
            "description": 
                "",
            "file": "image\\day3_evening"
        },
        "return": {
            "attraction": "返回飯店",
            "start_time": "21:00",
            "transport": "➡➡ 飯店"
        }
    },
    "2024-12-17": {
    },
    "2024-12-18": {
        "title": "前往土浦",
        "start": {
            "attraction": "ホテルグローバルビュー土浦",
            "alias": "土浦全球景觀飯店",
            "start_time": "09:00",
            "end_time": "12:00",
            "transport": "交通：飯店 ➖ 糀谷站 京急機場線 + 京急本線 13分 ➖ (轉車) 品川 常磐線 1小時26分 ➡➡ JR常磐線 土浦站",
            "description": 
                "周邊景點: 霞浦湖，日本第二大湖，適合騎自行車、釣魚等戶外活動。\n\n" +
                "預計住宿: 12-18 - 12-19，1晚",
            "file": "image\\day5_hotel"
        }
    },
    "2024-12-19": {
        "title": "返回台灣",
        "start": {
            "attraction": "土浦全球景觀飯店",
            "start_time": "08:00",
            "end_time": "10:00",
            "duration": "2 小時",
            "transport": "交通：飯店 ➖ 糀谷站 ➖ 京急本線 ➡➡ 羽田機場",
            "description": 
                "✔️ 退房手續，確保所有行李已打包完畢。\n\n" +
                "✈️ 準備前往羽田機場，搭乘預訂的返程班機。\n\n" +
                "📍 羽田機場地址: \n" +
                "https://www.google.com/maps/search/%E7%BE%BD%E7%94%B0%E6%A9%9F%E5%A0%B4",
            "file": "image\\day6_departure"
        },
        "return": {
            "attraction": "抵達台北桃園機場",
            "start_time": "12:00",
            "end_time": "15:00",
            "transport": "交通：➡➡ 飛機",
            "description": 
                "🎉 抵達台北桃園機場，結束愉快的東京之旅。\n\n" +
                "🏠 回到家中，整理旅遊回憶。",
            "file": "image\\day6_arrival"
        }
    }
}
