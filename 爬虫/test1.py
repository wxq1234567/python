import urllib.request
import urllib.parse
import json
# url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
url = "https://fanyi.baidu.com/sug"
data = {
    "kw": "black"
    # "from": "en",
    # "to": "zh",
    # "query": "black",
    # 'transtype': 'realtime',
    # 'simple_means_flag': '3',
    # 'sign': '689471.943630',
    # 'token': '404a2c5ffa62b8806ff23e0822e2e27e',
    # 'domain': 'common'
}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
info = bytes(urllib.parse.urlencode(data).encode('utf-8'))
request = urllib.request.Request(url, headers=header, data=info)
response = urllib.request.urlopen(request)
res = response.read().decode("utf-8")
print(json.loads(res))

