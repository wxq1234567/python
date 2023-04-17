import requests, csv, pymysql
from lxml import html
def arg1():
    # url = "http://www.go2.cn/search/all/?category_id=all&search_1=1&q=%E5%8D%95%E9%9E%8B&kl=hot"
    url = "http://www.go2.cn/search/all/page{}.html?category_id=all&search_1=1&q=%E5%8D%95%E9%9E%8B&kl=hot"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    for j in range(1, 7):
        request = requests.get(url.format(j), headers=header)
        request.encoding = 'utf-8'
        a = request.text
        res = html.etree.HTML(a)
        with open("aaa.csv", "w", newline="") as f:
            res2 = res.xpath('//ul[@class="clearfix"]/li')
            dict1 = []
            for i in res2:
                lj = i.xpath('.//div[@class="img-box"]/a/@href')
                if lj:
                    a = "http://www.go2.cn" + lj[0]
                    dict1.append(a)
                cate2 = i.xpath('.//a/img/@src')
                if cate2:
                    b = "http:" + cate2[0]
                    dict1.append(b)
                cate3 = i.xpath('.//div[@class="cont-wrap"]//span/text()')
                if cate3:
                    c = cate3[0]
                    dict1.append(c)
                    # print(cate3[0])
                cate4 = i.xpath('.//div[@class="pro-info app-text-nowrap"]/text()')
                if cate4:
                    d = cate4[0]
                    dict1.append(d)
                    # print(d)
                cate5 = i.xpath('.//div[@class="pro-name app-text-nowrap"]/text()')
                if cate5:
                    e = cate5[0]
                    dict1.append(e)
                print(dict1)
                row1 = csv.writer(f)
                row1.writerow(dict1)
# arg1()
def arg2():
    url = "http://www.go2.cn/search/all/page{}.html?category_id=all&search_1=1&q=%E5%8D%95%E9%9E%8B&kl=hot"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    # conn = pymysql.connect(host='localhost', user='root', password='123456', database='wxq', port=3306)
    # cursor = conn.cursor()
    for j in range(1, 7):
        request = requests.get(url.format(j), headers=header)
        request.encoding = 'utf-8'
        a = request.text
        res = html.etree.HTML(a)
        print(res)
        res2 = res.xpath('//div[@class="search-result-list"]/ul/li')
        # dict1 = {}
        # for i in res2:
        #     lj = i.xpath('.//div[@class="img-box"]/a/@href')[0]
        #     if lj:
        #         a = "http://www.go2.cn" + lj[0]
        #         dict1["链接"] = a
        #     cate2 = i.xpath('.//a/img/@src')
        #     if cate2:
        #         b = "http:" + cate2[0]
        #         dict1["图片"] = b
        #     cate3 = i.xpath('.//div[@class="cont-wrap"]//span/text()')
        #     if cate3:
        #         c = cate3[0]
        #         dict1["价格"] = c
        #     cate4 = i.xpath('.//div[@class="pro-info app-text-nowrap"]/text()')
        #     if cate4:
        #         d = cate4[0]
        #         dict1["介绍"] = d
        #         # print(d)
        #     cate5 = i.xpath('.//div[@class="pro-name app-text-nowrap"]/text()')
        #     if cate5:
        #         e = cate5[0]
        #         dict1["名字"] = e
        #     print(dict1)
        #     data = {k: '"' + str(v) + '"' for k, v in dict1.items()}
        #     print(data)
        #     if data:
        #         sql = f'INSERT INTO bbb(uname, lianjie, tp, jg, js) VALUES ({data["名字"]},{data["链接"]}, {data["图片"]},{data["价格"]}, {data["介绍"]});'
        #         cursor.execute(sql)
        #         conn.commit()
arg2()