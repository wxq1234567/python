import urllib.request
import urllib.parse
import json
# 地址
url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "BIDUPSID=90221932CDBB59A984699A64C6791BB3; PSTM=1646035667; BAIDUID=90221932CDBB59A9D302ECD218B812B7:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=90221932CDBB59A9D302ECD218B812B7:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664245825,1664325632; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664326014; ab_sr=1.0.1_MjQ0MDMzOGQyOGFiMzJkZGNkYmYwYjQwYmY1YWViOGNlNmM5ZmIxMjZkYTYxOTYxNGM5ZDljYzllYmNjNjBiYzg1YTJlZDJlNWZlN2I1MTNkYjYwMzQ5ZWM4ZjAyMThhZWZmOGUxZjEyNzI4NzU0NTIxYzA3Yjc3MzgxMWYyN2Y0YzkyZGM4ODRhOTY0N2NkMzZiYjNlYzg2MjM2NDJjMw=="
}
data = {
    "from": "en",
    "to": "zh",
    "query": "black",
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '689471.943630',
    'token': '404a2c5ffa62b8806ff23e0822e2e27e',
    'domain': 'common'
}
# 编码
info = bytes(urllib.parse.urlencode(data).encode('utf-8'))
# 构造request对象
request = urllib.request.Request(url, headers=header, data=info)
request.add_header("X-Requested-With", "XMLHttpRequest")
request.add_header("Cookie", "BIDUPSID=90221932CDBB59A984699A64C6791BB3; PSTM=1646035667; BAIDUID=90221932CDBB59A9D302ECD218B812B7:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=90221932CDBB59A9D302ECD218B812B7:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664245825,1664325632; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664326014; ab_sr=1.0.1_MjQ0MDMzOGQyOGFiMzJkZGNkYmYwYjQwYmY1YWViOGNlNmM5ZmIxMjZkYTYxOTYxNGM5ZDljYzllYmNjNjBiYzg1YTJlZDJlNWZlN2I1MTNkYjYwMzQ5ZWM4ZjAyMThhZWZmOGUxZjEyNzI4NzU0NTIxYzA3Yjc3MzgxMWYyN2Y0YzkyZGM4ODRhOTY0N2NkMzZiYjNlYzg2MjM2NDJjMw==")
# urlopen()
response = urllib.request.urlopen(request)
res = response.read().decode("utf-8")
print(json.loads(res))

