# requests 库

import requests

# 使用 requests 模拟浏览器爬取百度首页

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.97 Mobile Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding

# 查看响应的状态码

print(response.status_code)

# 查看响应的内容
print(response.text)

print(response.apparent_encoding)
