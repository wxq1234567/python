import requests
import json
# 带参数的get请求
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
url = "http://httpbin.org/get?name=王小全&age=18"
res1 = requests.get(url, headers=header)
res1.encoding = 'utf-8'
# print(json.loads(res1.text))

# 方法二
link = "http://httpbin.org/get"
par = {
    "name": "孙铭辰",
    "age": "18"
}
res2 = requests.get(link, params=par)
res2.encoding = 'utf-8'
# print(res2.text)

print(json.loads(res2.text))

