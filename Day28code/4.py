# 通过 urllib 模拟浏览器发送 POST 请求

from urllib import request, parse

url = "http://m.youdao.com/translate"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"
                  " Version/13.0.3 Mobile/15E148 Safari/604.1"
}

formdata = {
    "inputtext": "china",
    "type": "AUTO"
}

# URL编码转换
data = parse.urlencode(formdata).encode('utf-8')

print(data)

# 构造Request对象
request.Request(url, data=data, headers=headers)

response = request.urlopen(url, data)

print(response.status)

print(response.read().decode('UTF-8'))
