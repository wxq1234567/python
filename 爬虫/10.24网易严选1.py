import requests
import json
import re
import pymysql
class WY(object):
    def __init__(self):
        self.url = "https://you.163.com/xhr/globalinfo//queryTop.json"
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
            }
        self.conn = pymysql.connect(host='localhost', user='root', password="123456", database='wxq', port=3306)
        # 获取游标
        self.cursor = self.conn.cursor()
        self.list1 = []
    def get_cate1(self):
        request = requests.get(self.url, headers=self.header)
        request.encoding = 'utf-8'
        a = request.text
        res = json.loads(a)
        cateList = res["data"]["cateList"]
        for i in cateList:
            name = i["name"]
            subCateGroupList = i["subCateGroupList"]
            for j in subCateGroupList:
                name1 = j["name"]
                categoryList = j["categoryList"]
                # print(categoryList)
                for k in categoryList:
                    name2 = k["name"]
                    superCategoryId = k['superCategoryId']
                    id = k['id']
                    link = f"https://you.163.com/item/list?categoryId={superCategoryId}&subCategoryId={id}"
                    self.get_xinxi(link, name, name1, name2)
                    if len(self.list1) > 0:
                        for w in self.list1:
                            dat = {k: '"' + str(v) + '"' for k, v in w.items()}
                            sql = f'INSERT INTO hc1(name1,price,img,desc1) VALUES({dat["name"]},{dat["price"]},{dat["img"]},{dat["desc"]})'
                            self.save(sql)
        self.cursor.close()
        self.conn.close()
                    # print(link2)

    def get_xinxi(self, url, cate1, cate2, cate3):
        request = requests.get(url, headers=self.header)
        request.encoding = 'utf-8'
        a = request.text
        # res = a.split("var json_Data=")[1].split("json_Data.currentTimestamp")[0]
        res = re.findall(r"var json_Data=(.*)};", a)
        info = res[0] + "}"
        data = json.loads(info)
        # return data
        categoryItemList = data["categoryItemList"]
        for i in categoryItemList:
            itemList = i["itemList"]
            for j in itemList:
                good = {}
                name = j['name']
                simpleDesc = j['simpleDesc']
                retailPrice = j['retailPrice']
                scenePicUrl = j['scenePicUrl'] + '?type=webp&imageView'
                good['name'] = name
                good['desc'] = simpleDesc
                good['price'] = retailPrice
                good['img'] = scenePicUrl
                # good['cate1'] = cate1
                # good['cate2'] = cate2
                # good['cate3'] = cate3
                self.list1.append(good)
                # return self.list1
                # return name, retailPrice, scenePicUrl

    def save(self, sql):
        self.cursor.execute(sql)
        # 提交数据
        self.conn.commit()
aa = WY()
aa.get_cate1()


def get_cate2():
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    url = "https://you.163.com/"
    request = requests.get(url, headers=header)
    request.encoding = 'utf-8'
    a = request.text
    res = a.split("var JSON_DATA =")[1].split("</script>")[0]
    res1 = json.loads(res)
    cateList = res1["cateList"]
    # print(res)
    for i in cateList:
        name = i["name"]
        subCateList = i["subCateList"]
        for q in subCateList:
            name1 = q["name"]
            superCategoryId = q["superCategoryId"]
            id = q["id"]
            link2 = f"link3 = 'https://you.163.com/item/list?categoryId={superCategoryId}&subCategoryId={id}"
            print(name, name1, link2)
# get_cate2()


