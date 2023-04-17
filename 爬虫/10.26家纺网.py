import requests
from lxml import html

url = "http://detail.91jf.com/index/category_goods_list?category_id=102"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
request = requests.get(url, headers=header)
request.encoding = 'utf-8'
a = request.text
res = html.etree.HTML(a)
res1 = res.xpath('//div[@class="pro_list_div g-clearfix c"]//li[@class="goods_offset"]')

for i in res1:
    dict1 = {}
    res2 = i.xpath('.//div[@class="pro_pic_box"]//img/@src')
    if res2:
        a1 = res2[0]
        dict1["图片"] = a1
    res3 = i.xpath('.//div[@class="row row-1"]//b/text()')
    if res3:
        a2 = res3[0]
        dict1["价格"] = a2
    res4 = i.xpath('.//div[@class="row row-2 title"]/a/@title')
    if res4:
        a3 = res4[0]
        dict1["介绍"] = a3
    res5 = i.xpath('.//div[@class="row row-3 c"]/a/text()')
    if res5:
        a4 = res5[0]
        dict1["店铺"] = a4
    res6 = i.xpath('.//div[@class="row row-3 c"]//span/text()')
    if res6:
        a5 = res6[0]
        dict1["地址"] = a5
    print(dict1)
