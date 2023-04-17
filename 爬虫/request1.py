import requests
# 请求头信息
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
link = "https://www.baidu.com/"
# 发送get请求
response = requests.get(link, headers=header)
# 指定编码
response.encoding = 'utf-8'
print(response.text)



