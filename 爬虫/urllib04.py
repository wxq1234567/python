import urllib.request
import urllib.parse
link = "https://www.baidu.com/s?"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

dic = {
    "wd": "河南艺术职业学院"
}
a = urllib.parse.urlencode(dic)
b = "%E6%B2%B3%E5%8D%97%E8%89%BA%E6%9C%AF%E8%81%8C%E4%B8%9A%E5%AD%A6%E9%99%A2"
c = link + b
print(c)
request = urllib.request.Request(c, headers=header)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)
