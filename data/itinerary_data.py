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
            "transport": "交通：➡➡ 桃園機場",
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
            "transport": "交通：入境 ➖ 羽田機場 京急機場線 6分鐘 ➖ 糀谷站",
            "description": 
                "飯店的特色之一是設有名為「MANGA Library」的漫畫圖書館，收藏約8,000冊漫畫，供住客免費閱讀。\n\n" +
                "此外，飯店提供24小時的免費飲料吧，以及咖哩和烏龍麵等輕食服務，讓住客在任何時間都能享用。\n\n" +
                "預計住宿: 12-14 - 12-18，4晚"
                ,
            "file": "image\\day1_hotel"
        },
        "morning":{
            "attraction": "上野公園",
            "start_time": "08:00",
            "end_time": "14:00",
            "duration": "6 小時",
            "transport": "交通：飯店 ➖ 京急蒲田 9分鐘 ➖ (轉車) 品川 JY山手線 22分鐘 ➖ 鶯谷",
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
                "路線: https://myppt.cc/7zsOxT"
                ,
            "file": "image\\day1_morning"
        },
        "afternoon":{
            "attraction": "淺草",
            "start_time": "14:00",
            "end_time": "18:00",
            "duration": "4 小時",
            "transport": "交通：上野 ➖ 上野廣小路 銀座線 7分鐘 ➖ 淺草 ➡➡ 仲見世通 ➡➡ 淺草寺 ➡➡ 五重塔 ➡➡ 淺草西參道 ➡➡ 淺草文化觀光中心",
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
                        "➖➖ 花月堂: 波羅麵包\n\n"
                        ,
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
                    "➖ 天丼 金子半之助: 日本全國丼金賞獎，以原汁原味演繹江戶時代的傳統風味，重金自日本引進江戶時代獨家秘傳醬汁，並採用日本進口胡麻油\n\n"
                    ,
            "file": "image\\day1_evening"
        },
        "return":{
            "attraction": "返回飯店",
            "start_time": "22:00",
            "transport": "交通：押上 ➖ 押上 淺草線 + 京急本線 39分 ➖ 京急蒲田 ➡➡ 飯店"
        }
    },
    "2024-12-15": {
        "title": "箱根藝術與自然之旅：美術館、地熱奇觀與海盜船的獨特體驗",
        "start": {
            "attraction": "小原田站",
            "start_time": "08:00",
            "end_time": "09:30",
            "duration": "1.5 小時",
            "transport": "交通：飯店 ➖ 糀谷站 京急本線 12分 ➖ (轉車) 橫濱 東海道本線 52分 ➖ 小原田"
        },
        "morning": {
            "attraction": "箱根雕刻森林美術館",
            "start_time": "10:00",
            "end_time": "14:00",
            "duration": "4 小時",
            "transport": "交通：小原田 ➖ 箱根登山線 15分  ➖ (轉車) 箱根湯本 箱根登山線 36分  ➖ 雕刻之森 ➡➡ 箱根雕刻森林美術館",
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
            "transport": "交通：大湧谷 ➖ 箱根空中纜車 30分 ➖ 桃源台 ➖ (轉船) 海賊船 桃源臺港 ➡➡ 箱根海賊船 元箱根港",
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
                "交通：元箱根港 ➖ 元箱根港（バス）箱根町線：箱根口経由小田原駅行 57分 ➖ (轉車) 小田原 ➖ 東海道本線 50分 ➖ 橫濱\n\n" + 
                    "　　　　　" + 
                    "➡➡ (轉車) 港未來線各站停車元町、中華街 13分 ➖ 元町、中華街 ➡➡ 山下公園 ➡➡ 橫濱紅磚倉庫 ➡➡ 橫濱",
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
            "transport": "交通：橫濱 ➖ 京急本線 急行羽田機場 15分 ➖ 京急蒲田 ➡➡ 飯店"
        }
    },
    "2024-12-16": {
        "title": "",
        "morning": {
            "attraction": "三鷹之森吉卜力美術館",
            "start_time": "07:00",
            "end_time": "14:00",
            "duration": "5 小時",
            "transport": "交通：飯店 ➖ 京急蒲田 9分鐘 ➖ (轉車) 品川 JY山手線 18分鐘 ➖ (轉車) 代代木 中央‧總武線 21分 ➖ 吉祥寺\n\n "+
                    "　　　　　" + 
                    "➡➡ 井之頭恩賜公園 ➡➡ 三鷹之森吉卜力美術館",
            "description": 
                "購票:\n\n" +
                    "➖ 吉卜力美術館:\n\n" +
                        "➖➖ 注意: 每月10日開放隔月門票購買！！！！\n\n" +
                        "➖➖ 網站: https://l-tike.com/ghibli/\n\n" +
                        "➖➖ 教學: https://ectomy.pixnet.net/blog/post/43245418\n\n" 
                "景點:\n\n" +
                    "➖ 井之頭恩賜公園: 園內的井之頭池和三寶寺池、善福寺池並稱「武藏野三大湧水池」\n\n" +
                    "➖ 吉卜力美術館: 動畫工作室吉卜力的專屬博物館，內有手稿、動畫場景展示和小型電影院，營造出獨特的魔法世界。\n\n"
                    ,          
            "file": "image\\day3_morning"
        },
        "afternoon": {
            "attraction": "神樂坂",
            "start_time": "14:00",
            "end_time": "17:00",
            "duration": "3 小時",
            "transport": "交通：吉祥寺 ➖ 中央‧總武線 各站停車東西線 經由西船橋 12分鐘 ➖ 神樂坂 ➡➡ 東京大神宮 ➡➡ 靖國神社",
            "description": 
                "景點:\n\n" +
                    "➖ 神樂坂: 神樂坂是東京少數保留法式與日式混合風情的小巷\n\n" +
                    "➖ 東京大神宮: 動畫工作室吉卜力的專屬博物館，內有手稿、動畫場景展示和小型電影院，營造出獨特的魔法世界。\n\n" +
                    "➖ 靖國神社: 一座歷史悠久的神社，擁有壯觀的鳥居和主殿。\n\n" +
                "美食:\n\n" +
                    "➖ 神樂坂 茶寮: 傳統日式茶屋風格，提供抹茶甜點、抹茶拿鐵、和風甜品，特別推薦抹茶芭菲和日式甜點拼盤。\n\n" +
                    "➖ 広島お好み焼 くるみ: 正宗廣島燒\n\n" +
                    "➖ 離島廚房:  以日本各離島食材為主題，提供新鮮的海鮮料理。\n\n" +
                    "➖ 広島お好み焼 くるみ: 正宗廣島燒\n\n" +
                    "➖ 魚串さくらさく: 以海鮮串燒為主的居酒屋，提供新鮮的魚類串燒。\n\n"
                    ,          
            "file": "image\\day3_afternoon"
        },
        "evening":{
            "attraction": "秋葉原",
            "start_time": "17:00",
            "end_time": "21:00",
            "duration": "4 小時",
            "transport": "交通：九段下 ➖ 新宿線 本八幡 3分鐘 ➖ 小川町（東京） ➡➡ 秋葉原",
            "description":
                "景點:\n\n" +
                    "➖ 秋葉原電器街: 神樂坂是東京少數保留法式與日式混合風情的小巷\n\n" +
                    "➖ Animate: 動畫、漫畫相關商品的大型連鎖店\n\n" +
                    "➖ Mandarake: 二手動漫、模型、遊戲、DVD 等的店鋪\n\n" +
                    "➖ AKB48 Cafe & Shop: AKB48的專屬咖啡店與商店\n\n" +
                    "➖ @Home Maid Cafe: 女僕咖啡廳文化\n\n" +
                    "➖ 秋葉原Radio Kaikan: 綜合性動漫商店大樓\n\n" +
                    "➖ Sega 秋葉原: 人氣最高的遊戲中心\n\n" +
                    "➖ Super Potato：專賣復古遊戲和主機的商店，吸引許多遊戲迷。" +
                    "➖ mAAch ecute 神田萬世橋：由舊萬世橋車站改建而成的文創商場，保留了歷史建築的特色。\n\n" +
                    "➖ 2k540 AKI-OKA ARTISAN: 鐵路高架橋下的手工藝品商場"
                    ,
            "file": "image\\day3_evening"
        },
        "return": {
            "attraction": "返回飯店",
            "start_time": "22:30",
            "transport": "秋葉原 ➖ 山手線 東京/品川方面(外環線) 17分➖ (轉車) 品川 京急本線 11分 ➖ 京急蒲田 ➡➡ 飯店",
        }          
    },

    "2024-12-17": {
        "title": "東京風格與風味：建築之美與美食饗宴",
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
                    "➖ 築地黑銀鮪魚屋: 以新鮮現切的鮪魚生魚片和壽司聞名\n\n"
                    ,          
            "file": "image\\day4_morning_1"
        },
        "morning_2": {
            "attraction": "新宿御苑",
            "start_time": "09:00",
            "end_time": "13:00",
            "duration": "4 小時",
            "transport": "築地市場 大江戶線 大門/六本木方面 16分 ➖ 國立競技場 ➡➡ 新宿御苑 ➡➡ 花園神社 ➡➡ 思い出橫丁（回憶橫丁）",
            "description": 
                "景點: \n\n" +
                    "➖ 新宿御苑: 融合日式、英式和法式風格的大型庭園。\n\n" +
                    "➖ 花園神社: 在德川家康時期創建的鎮守神社，主要供奉日本神衹「倉稻魂命」、「日本武」和「受持神」\n\n" +
                    "➖ 回憶橫丁: 充滿昭和時代風情，擁有許多小型居酒屋和餐館，適合體驗日本傳統飲食文化。\n\n" + 
                "美食: \n\n" +
                    "➖ かめや: 蕎麥麵店以平價美味著稱，特別是「天玉そば」（炸蔬菜天婦羅加溫泉蛋蕎麥麵）\n\n" +
                    "➖ 岐阜屋: 這家中華料理店提供各式麵類、煎餃和炒飯，其中「豬肉木耳炒蛋」是必點菜色。\n\n" +
                    "➖ 鳥園: 以烤雞串聞名，提供多樣的串燒選擇。\n\n"
                    ,
            "file": "image\\day4_morning_2"
        },
        "afternoon": {
            "attraction": "表參道",
            "start_time": "13:00",
            "end_time": "17:00",
            "duration": "4 小時",
            "transport": "交通：新宿 ➖ 山手線各站停車品川 / 澀谷方面(內環線) 5分 ➖ 原宿 ➡➡ 明治神宮 ➡➡ 表參道",
            "description":
                "景點:\n\n" +
                    "➖ 明治神宮: 祭祀明治天皇與昭憲皇太后的神社，大鳥居、寶物殿\n\n" +
                    "➖ 表參道: 東京著名的時尚街區，兩旁林蔭大道上聚集了眾多精品店和咖啡廳\n\n"
                        "➖➖ 表參道之丘: 安藤忠雄設計的購物中心\n\n" +
                        "➖➖ HARAKADO 原角: 中村拓志『戀建築』\n\n" +
                        "➖➖ 根津美術館: 隈研吾『負建築』\n\n" +
                "美食\n\n" +
                    "➖ Pierre Hermé Paris 青山: 法國知名甜點店，提供精緻馬卡龍和法式甜點\n\n" +
                    "➖ Afternoon Tea • LOVE & TABLE: 結合甜甜圈與咖啡的專賣店\n\n" +
                    "➖ 裏參道GARDEN: 日式老宅內的咖啡廳，提供傳統和風甜點，如米粉鬆餅和水信玄餅\n\n" +
                    "➖ GARIGUETTE: 以圓形法式千層酥聞名\n\n" +
                    "➖ CHAVATY: 專注於茶飲的咖啡廳，提供錫蘭烏瓦紅茶、京都焙茶和宇治抹茶等多款奶茶，並搭配司康等甜點\n\n" +
                    "➖ Ginger Garden AOYAMA: 以創意主打的貴婦感滿點的咖啡廳\n\n" +
                    "➖ FRUIT PICNIC: 以草莓為主題的咖啡廳，內部裝潢充滿童話氛圍\n\n" 
                ,
            "file": "image\\day4_afternoon"
        },
        "evening": {
            "attraction": "渋谷",
            "alias": "澀谷",
            "start_time": "17:00",
            "end_time": "20:00",
            "duration": "3 小時",
            "transport": "交通：表參道 ➖ 銀座線澀谷 2分 ➖ 澀谷",
            "description": 
                "景點:\n\n" +
                    "➖ 渋谷十字路口: 世界上最繁忙的十字路口之一，每當行人信號燈轉綠，數百人同時穿越馬路，場面壯觀。附近的咖啡店如「星巴克」提供俯瞰交叉口的絕佳視角。\n\n" +
                    "➖ 澀谷Stream: 新興的複合設施，內有餐廳、酒店和辦公室，並設有沿河的步道，提供悠閒的散步環境。\n\n" +
                    "➖ 澀谷HIKARIE: 購物、餐飲、藝術於一體的綜合設施。其內的展望台「スカイロビー」可免費欣賞渋谷全景。\n\n" +
                    "➖ 澀谷Mark City: 有多樓層的購物和餐飲中心，地下層設有直通澀谷站的美食廣場。\n\n" +
                    "➖ MEGA唐吉訶德 澀谷本店 : 東京都內最大的驚安殿堂，24小時營業，店面超大、商品更多\n\n" +
                    "➖ 澀谷PARCO :「澀谷PARCO」首家任天堂、寶可夢旗艦店進駐\n\n" +
                    "➖ 青の洞窟 SHIBUYA - DAY＆NIGHT: 澀谷青之洞窟點燈企劃從2014年開始在中目黑實施，2016～2019年移師至澀谷。\n\n"                   
                ,
            "file": "image\\day4_evening"
        },
        "return": {
            "attraction": "返回飯店",
            "start_time": "20:00",
            "transport": "澀谷 ➖ 銀座線各站停車淺草 17分 ➖ 京橋（東京） ➡➡ 東京車站 ➖ 山手線 9分➖ (轉車) 品川 京急本線 11分 ➖ 京急蒲田 ➡➡ 飯店",
            "description": 
                "景點:\n\n" +
                    "➖ 東京車站點燈: 丸之內香檳金樹步道\n\n" +
                    "➖ 馬力歐點燈活動: https://www.marunouchi.com/pickup/event/4432/\n\n" +                   
                    "➖ Garden Terrace: 新丸之內大樓7樓露台\n\n" +
                    "➖ KITTE: KITTE商場6樓的屋頂庭園\n\n"
               ,
            "file": "image\\day4_night"
        }
    },
    "2024-12-18": {
        "title": "茨城土浦",
        "start": {
            "attraction": "ホテルグローバルビュー土浦",
            "alias": "土浦全球景觀飯店",
            "start_time": "08:00",
            "end_time": "10:00",
            "duration": "2 小時",
            "transport": "交通：飯店 ➖ 糀谷站 京急機場線 + 京急本線 13分 ➖ (轉車) 品川 常磐線 1小時26分 ➖ JR常磐線 土浦站 ➡➡ 飯店",
            "description": 
                "✔️ 退房手續，確保所有行李已打包完畢。\n\n" +
                "預計住宿: 12-18 - 12-19，1晚\n\n"
                ,
            "file": "image\\day5_hotel"
        },
        "morning": {
            "attraction": "霞浦湖",
            "start_time": "10:00",
            "end_time": "12:00",
            "duration": "2 小時",
            "transport": "飯店 ➡➡ 土浦港",
            "description": 
                "活動:\n\n" +
                    "➖ 霞浦湖遊覽船: 日本第二大湖，郵船時間約30分鐘。\n\n" +
                    "➖➖ 行程: 土浦港→舊予科練沖→霞浦沖→筑波山展望→土浦港" +
                    "➖➖ 網站: https://visit.ibarakiguide.jp/zh-hant/sightseeing/22847/。\n\n" +
                "美食:\n\n" +
                    "目利的銀次 ➖ 提供新鮮海鮮和創意料理\n\n"
                "預計住宿: 12-18 - 12-19，1晚\n\n"
                ,
            "file": "image\\day5_morning"           
        },
        "afternoon": {
            "attraction": "偕樂園",
            "start_time": "12:00",
            "end_time": "15:00",
            "duration": "3 小時",
            "transport": "土浦 ➖ 常磐線 勝田 42分 ➖ 水戶 ➖ (轉公車) 偕楽園～払沢・本郷～偕楽園偕楽園行 9分 ➖ 常磐神社入口［神崎寺前］ ➡➡ 偕樂園",
            "description": 
                "景點:\n\n" +
                    "➖ 偕樂園: 與金澤的兼六園、岡山的後樂園並列為日本三大名園之一\n\n" +
                    "➖ 好文亭: 位於偕樂園內的木造建築，曾是水戶藩主德川齊昭接待賓客的場所。\n\n" +
                    "➖ 千波湖:  位於市中心的天然湖泊，周圍設有步道和公園，是市民休閒散步的好去處。\n\n" +
                    "➖ 常磐神社: 供奉水戶藩主德川光圀（即水戶黃門）和德川齊昭。神社內的義烈館展示了與水戶黃門相關的歷史文物。\n\n" +
                    "➖ 茨城縣近代美術館: 收藏了明治時期以來的多件藝術作品。\n\n"
                ,
            "file": "image\\day5_afternoon"           
        },
        "evening": {
            "attraction": "大洗",
            "start_time": "15:00",
            "end_time": "19:00",
            "duration": "4 小時",
            "transport": "水戸駅（北口） ➖ 茨大前～水戸駅～アクアワールドアクアワールド・大洗 33分 ➖ 大洗神社前 ➡➡ 大洗磯前神社\n\n" +
                    "　　　　　" + 
                    "➡➡ 大洗神社前 ➖ 茨大前～アクア～那珂湊駅茨大前営業所 6分 ➖ 磯浜新道 ➡➡ 大洗 SEASIDE STATION",
            "description": 
                "景點:\n\n" +
                    "➖ 大洗磯前神社: 以佇立於海中礁石上的「神磯鳥居」聞名，特別是在日落時分，景色尤為壯麗。\n\n" +
                    "➖ 大洗海洋塔: 高達60米，以其獨特的三角形玻璃外觀而聞名。塔內設有觀景台、餐廳和商店，提供多元的觀光體驗。\n\n" +
                    "➖ 大洗 SEASIDE STATION: 大洗町的海濱購物中心，於 2018 年重新開幕，成為當地的潮流地標。商場分為兩層樓，匯集多家商店和餐廳，提供多樣化的購物與美食選擇。\n\n"
                ,
            "file": "image\\day5_evening"           
        },
        "return": {
            "attraction": "返回飯店",
            "start_time": "18:00",
            "transport": "磯浜新道 ➖ 水戸駅～大洗ＦＴ～那珂湊駅水戸駅（北口） 27分 ➖ 水戸駅（北口） ➖ (轉車)常磐線上野 43分 ➖ 土浦 ➡➡ 飯店"
        }
    },
    "2024-12-19": {
        "title": "返回台灣",
        "morning": {
            "attraction": "石岡",
            "start_time": "10:00",
            "end_time": "12:00",
            "duration": "2 小時",
            "transport": "飯店 ➡➡ 土浦港",
            "description": 
                "景點:\n\n" +
                    "➖ 石岡老街: 昭和時代風情的老街，保留了許多融合洋風與和風特色的「看板建築」\n\n"
                ,
            "file": "image\\day6_morning"           
        },
        "afternoon": {
            "attraction": "茨城機場",
            "start_time": "12:00",
            "end_time": "18:00",
            "duration": "6 小時",
            "transport": "交通：石岡 ➖ 茨城機場交通車機場接駁巴士 35分 ➖ 茨城空港",
            "description": 
                "⚠️ 重要訊息 \n\n" +
                "➖ 請務必準時抵達機場於班機起飛前2.5小時開始辦理櫃台報到及行李託運手續，請旅客務必於起飛前 45 分鐘完成報到\n\n" +
                "➖ 航班時間: 15:00，請於 13:00 開始進行報到。\n\n" +
                "📶 WIFI" +
                    "➖ 歸還地點: 桃園機場第一航廈"
                ,
        }
    }
}
