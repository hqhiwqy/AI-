# urllib 官方库

# py2里是urllib2  py3里是urllib

# 快速爬取一个百度首页

from urllib import request

url = "https://www.baidu.com/"

response = request.urlopen(url)

# 返回码  如果是200就代表成功
print(response.status)

# 获取网页内容

html = response.read().decode('utf-8')

print(html)