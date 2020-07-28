# requests 库

import requests

# 使用 requests 爬取百度首页

url = "https://www.baidu.com"

response = requests.get(url)
response.encoding = response.apparent_encoding
# response.encoding = 'utf-8'

# 查看响应的状态码

print(response.status_code)

# 查看响应的内容
print(response.text)

print(response.apparent_encoding)