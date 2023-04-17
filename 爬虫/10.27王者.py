import requests
from lxml import html
import pymysql, csv, json

def get_hero():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

    }
    conn = pymysql.connect(host='localhost', user='root', password='123456', database='wxq', port=3306)
    cursor = conn.cursor()
    url = "https://pvp.qq.com/web201605/herolist.shtml"
    # 需要传递的参数
    res = requests.post(url, headers=header)
    res.encoding = 'gbk'
    a = res.text
    res = html.etree.HTML(a)
    res1 = res.xpath('//ul[@class="herolist clearfix"]/li')
    for i in res1:
        dict1 = {}
        res2 = i.xpath('.//img/@src')
        dict1["图片"] = res2[0]
        res3 = i.xpath('.//a/text()')
        dict1["名字"] = res3[0]
        data = {k: '"' + str(v) + '"' for k, v in dict1.items()}
        # print(dict1)
        sql = f'INSERT INTO yx( namel, img) VALUES ({data["名字"]},{data["图片"]});'
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()
# get_hero()

def get_hero2():
    url = "https://pvp.qq.com/web201605/js/herolist.json"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    url2 = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/{}/{}.jpg"
    url3 = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-1.jpg"
    request = requests.get(url, headers=header)
    request.encoding = 'utf-8'
    a = request.text
    res = json.loads(a)
    a1 = []
    for i in res:
        res1 = i["ename"]
        res2 = i["cname"]
        res3 = url2.format(res1, res1)
        res4 = url3.format(res1, res1)
        print(res2, res3, res4)
        # a1.append(res1)
    # with open("yyy.csv", "a", newline="") as f:
    #     row1 = csv.writer(f)
    #     row1.writerow(a1)
    # f.close()
get_hero2()