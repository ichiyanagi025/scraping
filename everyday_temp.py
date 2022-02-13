import WebScraping as WS
import LINE as LI

address = 9891607
url = WS.wether_url(address)
today_list = WS.get_temp(url)
print(today_list)
txt = ["今日の気温は",
"予想最高"+today_list[0]+"度",
"予想最低"+today_list[1]+"度"]
for t in txt:
    LI.txt(t)