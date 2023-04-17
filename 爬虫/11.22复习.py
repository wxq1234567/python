import requests
from lxml import html
import json,csv


def qwe():
    url = "http://detail.91jf.com/"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    request = requests.get(url, headers=header)
    request.encoding = 'utf-8'
    a = request.text
    # print(a)
    res = html.etree.HTML(a)
    res2 = res.xpath('//div[@class="index_g_class"]/ul/li')
    for i in res2:
        cate1 = i.xpath('.//a/span/text()')[0]
        # print(cate1)
        cate2 = i.xpath('.//a/span/text()')[1:][0]
        # print(f"一级类目：{cate1}，二级类目：{cate2}")
        res3 = i.xpath('.//div[@class="class_child_li"]/ul/li')
        for j in res3:
            cate3 = j.xpath('.//a/span/text()')[0]
            print(f"一级类目：{cate1}，二级类目：{cate2}，三级类目:{cate3}")

# qwe()

with open('家纺.csv','w',newline="") as f:
    a = ["一级类目", "二级类目", "三级类目"]
    row1 = csv.writer(f)
    row1.writerow(a)
    url = "https://you.163.com/xhr/globalinfo//queryTop.json?__timestamp=1669099537038"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    request = requests.get(url, headers=header)
    request.encoding = 'utf-8'
    a = request.text
    # print(a)
    res = json.loads(a)
    data = res["data"]["cateList"]
    for i in data:
        cate1 = i["name"]
        # print(cate1)
        subCateGroupList = i["subCateGroupList"]
        for j in subCateGroupList:
            cate2 = j["name"]
            # print(cate1,cate2)
            categoryList = j["categoryList"]
            for s in categoryList:
                cate3 = s["name"]
                print(cate1,cate2,cate3)
                b = [cate1,cate2,cate3]
                row1.writerow(b)



