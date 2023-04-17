# https://pvp.qq.com/web201605/herodetail/135.shtml
import requests
import json
from lxml import html

url = "https://pvp.qq.com/web201605/js/herolist.json"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
url2 = "https://pvp.qq.com/web201605/herodetail/{}.shtml"
# url2 = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/{}/{}.jpg"
# url3 = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-1.jpg"
request = requests.get(url, headers=header)
request.encoding = 'utf-8'
a = request.text
res = json.loads(a)

for i in res:
    res1 = i["ename"]
    res2 = i["cname"]
    res3 = url2.format(res1)
    # res4 = url3.format(res1, res1)
    # print(res1, res2, res3)
    res5 = requests.get(res3, headers=header)
    res5.encoding = 'gbk'
    arg = html.etree.HTML(res5.text)
    # print(arg)
    # arg1 = arg.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/li')
    # for j in arg1:
    #     arg2 = i.xpath('.//i/img/@src')
    #     print(arg2)
    for a1 in range(10):
        if a1 < 10:
            img = f"https://game.gtimg.cn/images/yxzj/img201606/heroimg/{res1}/{res1}-smallskin-{a1}.jpg"
        else:
            img = f"https://game.gtimg.cn/images/yxzj/img201606/heroimg/{res1}/{res1}-smallskin-{a1}.jpg"
        res2 = requests.get(img, headers=header)  # 请求图片地址
        if res2.status_code == 200:
            with open(f"img/{res2}", "ab") as f:
                f.write(res2.content)


