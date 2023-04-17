import urllib.parse
import urllib.request
import requests
import pymongo
import json

url = "https://weibo.com/ajax/side/hotSearch"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
# 指定数据库
db = conn.wxqdb
# 指定集合
wb = db.weibo
request = requests.get(url, headers=header)
a = request.text
res = json.loads(a)
data = res['data']
res1 = data["realtime"]
# print(res1)
for b in res1:
    dict1 = {}
    note = b["note"]
    print(note)
    word_scheme = b["word_scheme"]
    print(word_scheme)
    dic = {
        "q": note
    }
    a = urllib.parse.urlencode(dic)
    link = f"https://s.weibo.com/weibo?{a}%23&topic_ad="
    print(link, note)
    dict1["note"] = note
    dict1["link"] = link
    wb.insert_one(dict1)
