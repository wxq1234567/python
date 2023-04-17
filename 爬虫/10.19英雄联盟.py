import requests
import json
import csv
img_link = "https://game.gtimg.cn/images/lol/act/img/skin/big"
url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=11"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
request = requests.get(url, headers=header)
request.encoding = 'utf-8'
a = request.text
res = json.loads(a)
hero = res['hero']
# print(type(hero))
# with open("hero.csv", "a", newline="") as f:
#     a2 = ["id", "名字", "alias", "title"]
#     row1 = csv.writer(f)
#     row1.writerow(a2)
#     for i in hero:
#         heroId = i["heroId"]
#         name = i["name"]
#         alias = i["alias"]
#         title = i["title"]
#         a1 = [heroId, name, alias, title]
#         print(a1)
#         row1 = csv.writer(f)
#         row1.writerow(a1)
# f.close()
# 获取皮肤
for i in hero:
    heroId = i["heroId"]
    name = i["name"]
    alias = i["alias"]
    title = i["title"]
    print(heroId, name, alias, title)
#     img = img_link + heroId + "000.jpg"  # 拼接土图片地址
#     # 获取每一个英雄的第一个皮肤并写入本地
#     res1 = requests.get(img)  # 请求图片地址
#     if res1.status_code == 200:
#         # 写入图片 二进制 # res1.content
#         with open(f"img/{name}.jpg", "wb") as f:
#             f.write(res1.content)
#     # 	https://game.gtimg.cn/images/lol/act/img/skin/big1000.jpg
#     # https://game.gtimg.cn/images/lol/act/img/skin/big2000.jpg
# 获取多个皮肤
# https://game.gtimg.cn/images/lol/act/img/skin/big2000.jpg
# https://game.gtimg.cn/images/lol/act/img/skin/big2001.jpg
    for a1 in range(100):
        if a1 < 10:
            img = img_link + heroId + "00" + str(a1) + ".jpg"
        else:
            img = img_link + heroId + "0" + str(a1) + ".jpg"
        res2 = requests.get(img, headers=header)  # 请求图片地址
        if res2.status_code == 200:
            with open(f"img/{alias}" + str(a1) + ".jpg", "ab") as f:
                f.write(res2.content)




