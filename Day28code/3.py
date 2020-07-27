# 通过 urllib 模拟浏览器发送 POST 请求

from urllib import request, parse


url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.97 Safari/537.36"
}

formdata = {
    "i": "china",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15953268438923",
    "sign": "4a104c0e6a3ec198fa7cd0c24bb5ce01",
    "ts": "1595326843892",
    "bv": "41db12f644f9bbe039ea4051ed753e63",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION"
}


# URL编码转换
data = parse.urlencode(formdata).encode('utf-8')

print(data)

# 构造 Request 对象
request.Request(url, data=data, headers=headers)

response = request.urlopen(url, data)

print(response.status)

print(response.read().decode('UTF-8'))