import requests
from lxml import html
url = "https://www.jd.com/"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

request = requests.get(url, headers=header)
request.encoding = 'utf-8'
a = request.text
res = html.etree.HTML(a)
res1 = res.xpath('//li[@class="cate_menu_item"]/a/text()')
print(res1)
