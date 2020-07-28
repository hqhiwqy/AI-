# 使用 urllib 库模拟浏览器发送 GET 请求

# 爬取百度中"Python"关键字的搜索结果网页

import urllib.parse, urllib.request

url = "https://www.baidu.com/s"

word = {
    "wd": "Python"
}

# 转换成url编码格式（字符串）

word = urllib.parse.urlencode(word)

print(word)

new_url = url + "?" + word

print(new_url)

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.97 Mobile Safari/537.36"
}

# 构造 request 对象
request = urllib.request.Request(new_url, headers=headers)

response = urllib.request.urlopen(request)

# 使用read()方法读取获取网页的内容，同时使用 UTF-8 格式进行解码
html = response.read().decode('UTF-8')

print(html)
