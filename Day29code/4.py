# 使用 requests 库模拟浏览器发送 GET 请求

# 爬取百度中"Python"关键字的搜索结果网页

import requests

url = "https://www.baidu.com/s"

word = {
    "wd": "Python"
}

# header请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.97 Mobile Safari/537.36"
}

# 发送 GET 请求，返回一个响应对象
response = requests.get(url, params=word, headers=headers)
response.encoding = response.apparent_encoding

# 查看响应的内容
print(response.text)
