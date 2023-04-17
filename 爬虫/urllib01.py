import urllib.request

# response = urllib.request.urlopen('http://www.baidu.com')
# html = response.readline().decode('utf-8')
# # print(html)
# print(type(response))
# print(response.geturl())  # 请求网址
# print(response.getcode())  # 状态码
# print(response.info())  # 网页元信息


# res = urllib.request.urlopen('http://python.org')
# ht = res.read().decode('utf-8')
# print(res.geturl())
# print(res.getcode())
# print(res.info())
# link = 'http://www.baidu.com'
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
# }
# request = urllib.request.Request(link, headers=header)
# response = urllib.request.urlopen(request)
# html = response.read().decode("utf-8")
# print(type(response))
# print(response.geturl())  # 请求网址
# print(response.getcode())  # 状态码
# print(response.info())  # 网页元信息

import urllib.parse
info = {
    "名字": "王梦娇",
    "班级": "二班"
}
res = urllib.parse.urlencode(info)  # 编码
da = urllib.parse.unquote(res)  # 解码
print(res)
print(da)


