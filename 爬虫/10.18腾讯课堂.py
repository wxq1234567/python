import requests
import pymysql
from lxml import html
class Python1(object):
    def __init__(self):
        self.url = "https://ke.qq.com/course/list?mt=1001&st=2064"
        self.header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
        self.conn = pymysql.connect(host='localhost', user='root', password='123456', database='wxq', port=3306)
        self.cursor = self.conn.cursor()
        self.links = []

    def cate(self):
        self.jx()  # 调用jx方法
        for a1 in self.links:
            request = requests.get(a1, headers=self.header)  # aaa是拼接所有的界面url
            request.encoding = 'utf-8'
            a = request.text
            res = html.etree.HTML(a)
            res1 = res.xpath('//div[@class="course-list"]/div')
            dict1 = {}
            for i in res1:
                res2 = i.xpath('.//div[@class="kc-course-card-content"]/h3/@title')
                if len(res2) > 0:
                    res2 = res2[0]
                    dict1["name"] = res2
                else:
                    dict1["name"] = ""
                res3 = i.xpath('.//a[@class="kc-course-card js-report-link kc-list-course-card kc-course-card-column"]/@href')
                if len(res3) > 0:
                    res3 = self.url + res3[0]
                    dict1["价格"] = res3
                else:
                    dict1["价格"] = ""
                # print(dict1)

                data = {k: '"' + str(v) + '"' for k, v in dict1.items()}
                sql = f'INSERT INTO s( namel, price) VALUES ({data["name"]},{data["价格"]});'
                self.my(sql)  # 调用sql方法
        self.cursor.close()
        self.conn.close()
    def jx(self):
        request = requests.get(self.url, headers=self.header)
        request.encoding = 'utf-8'
        a = request.text
        res = html.etree.HTML(a)
        res5 = res.xpath('//li/a[@rel="nofollow"]/text()')
        res6 = int(res5[-1])
        for h in range(1, res6+1):
            url2 = self.url + '&page=' + str(h)
            self.links.append(url2)

    def my(self, sql1):
        self.cursor.execute(sql1)
        self.conn.commit()  # 提交

py = Python1()
py.cate()
