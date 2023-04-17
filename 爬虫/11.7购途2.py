import pymysql
import requests, csv
from lxml import html

url = "http://www.go2.cn/search/all/page{}.html?category_id=all&search_1=1&q=%E5%8D%95%E9%9E%8B&kl=hot"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

conn = pymysql.connect(host="localhost", user="root", password="123456", database="wxq", )