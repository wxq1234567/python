from lxml import html
doc = """
<div>
    <ul class="item">
        <li class="item-0">
            <a href="link1.html">first item</a>
        </li>
        <li class="item-1">
            <a href="link2.html">second item</a>
        </li>
        <li class="item-inactive">
            <a href="link3.html">third item</a>
        </li>
        <li class="item-1">
            <a href="link4.html">fourth item</a>
        </li>
        <li class="item-0">
            <a href="link5.html">fifth item</a>
        </li>
    </ul>
 </div>
"""
page = html.etree.HTML(doc)  # 将响应结果转化为文档树对象
# 获取所有的li标签
# li = page.xpath('//li')
# li = page.xpath('//ul/li')
# li = page.xpath('//div/ul/li')
# 获取所有的a标签
a = page.xpath('//li/a')
# 获取a标签属性
shu = page.xpath("//li/a/@href")
# 获取a标签文字信息
wz = page.xpath("//li/a/text()")
# 获取最后一个a标签的文字信息
# la = page.xpath("//li/a/text()")[-1]
# la = page.xpath("//li[last()]/a/text()")
# print(la)

# 获取所有li标签的class名
na = page.xpath("//li/@class")
# print(na)

# 获取最class是 item-0 的li标签下的a标签的href属性
b = page.xpath('//li[@class="item-0"]/a/@href')
# print(b)
# 获取 任意 class 是item 的ul标签下 href属性是link4.html 的a标签的文字信息
c = page.xpath('//ul[@class="item"]//a[@href="link4.html"]/text()')
# print(c[0])
# contains
# con = page.xpath('//*[contains(@class,"item")]')
# print(len(con))

res1 = page.xpath('//a[contains(@href,"link")]')
# print(len(res1))
# starts-with
le = page.xpath('//*[starts-with(@href,"l")]')
print(len(le))
# 前两个li标签下的a标签的文本信息
res2 = page.xpath("//li/a/text()")[:2]
print(res2)
