import requests
import json
import re
import pymongo
url = "https://you.163.com/item/list?categoryId=1005002&_stat_area=nav_5&_stat_referer=index"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
# conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
# # 指定数据库
# db = conn.wxqdb
# # 指定集合
# wy = db.wangyi
request = requests.get(url, headers=header)
request.encoding = 'utf-8'
a = request.text
# print(a)
res = re.findall(r"var json_Data=(.*)};", a)
info = res[0] + "}"
data = json.loads(info)
categoryItemList = data["categoryItemList"]
# print(categoryItemList)
for i in categoryItemList:
    a = i["itemList"]
    # print(a)
    for j in a:
        # name = j["name"]
        # retailPrice = j["retailPrice"]
        # simpleDesc = j["simpleDesc"]
        # productPlace = j["productPlace"]
        # listPicUrl = j["listPicUrl"] + "?type=webp&quality=95&imageView"
        # print(name,retailPrice, simpleDesc, productPlace, listPicUrl)
        dict1 = {}
        dict1["name"] = j["name"]
        dict1["retailPrice"] = j["retailPrice"]
        dict1["simpleDesc"] = j["simpleDesc"]
        dict1["productPlace"] = j["productPlace"]
        dict1["listPicUrl"] = j["listPicUrl"] + "?type=webp&quality=95&imageView"
        print(dict1["name"], dict1["retailPrice"], dict1["simpleDesc"], dict1["productPlace"], dict1["listPicUrl"])
        # wy.insert_one(dict1)


