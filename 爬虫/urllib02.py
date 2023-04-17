import urllib.request
import urllib.parse
s = "https://fanyi.baidu.com/sug"
info = {
    "kw": "你"
}
data = bytes(urllib.parse.urlencode(info).encode("utg-8"))

header = {

}

