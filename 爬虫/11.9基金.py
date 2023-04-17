import requests
import json, csv

with open("基金.csv", "w", newline="") as f:
    row1 = csv.writer(f)
    a = ["基金代码", "基金简称", "期间涨幅", "期间分红", "分红次数", "起始日期", "单位净值", "累计净值", "终止日期", "单位净值", "累计净值", "成立日期", "手续费"]
    row1.writerow(a)
    for j in range(1, 4):
        print(j)
        url = f"http://fund.eastmoney.com/data/rankhandler.aspx?op=dy&dt=kf&ft=all&rs=&gs=0&sc=qjzf&st=desc&sd=2021-11-09&ed=2022-11-09&es=0&qdii=&pi={j}&pn=50&dx=0&v=0.43802996478302525"
        # http://fund.eastmoney.com/data/rankhandler.aspx?op=dy&dt=kf&ft=all&rs=&gs=0&sc=qjzf&st=desc&sd=2021-11-09&ed=2022-11-09&es=0&qdii=&pi=2&pn=50&dx=0&v=0.8367042096800343
        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "Referer": "http://fund.eastmoney.com/data/diyfundranking.html"
        }
        request = requests.get(url, headers=header)
        request.encoding = 'utf-8'
        a = request.text
        res = a.split("{datas:[")[1].split("],allRecords:16108")[0]
        # data = json.loads(a)
        res2 = res.split('",')
        # print(res)
        for i in res2:
            # w = []
            a = i.replace('"', "").split(",")
            # print(a)
            # w.append(a)
            # print(w)
            row1.writerow(a)

