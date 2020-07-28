# 使用 requests 模拟浏览器发送 POST 请求

import requests

url = "http://m.youdao.com/translate"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"
                  " Version/13.0.3 Mobile/15E148 Safari/604.1"
}

formdata = {
    "inputtext": "china",
    "type": "AUTO"
}

response = requests.post(url, data=formdata)
response.encoding = response.apparent_encoding

print(response.text)