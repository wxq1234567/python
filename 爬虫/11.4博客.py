import requests
from lxml import html
url = "https://www.cnblogs.com/"
link = "https://www.cnblogs.com/sitehome/p/{}"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
for j in range(1, 5):
    url2 = link.format(j)
    print(url2)
    request = requests.get(url2, headers=header)
    request.encoding = 'utf-8'
    a = request.text
    res = html.etree.HTML(a)
    res2 = res.xpath('//div[@id="post_list"]/article')
    for i in res2:
        res3 = i.xpath('.//div[@class="post-item-text"]/a/text()')[0]
        res4 = i.xpath('.//div[@class="post-item-text"]/a/@href')[0]
        print(res3, res4)

