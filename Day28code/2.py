# 通过urllib 模拟浏览器发送 GET 请求

from urllib import request

url = "http://www.baidu.com"

# 构造 Request 对象
Request = request.Request(url)
Request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, '
                                 'like Gecko) Chrome/78.0.3904.108 Safari/537.36')

response = request.urlopen(Request)

print(response.status)

print(response.read().decode('utf-8'))