import requests

url = "https://p0.meituan.net/movie/4c41068ef7608c1d4fbfbe6016e589f7204391.jpg@160w_220h_1e_1c"

response = requests.get(url)

# print(response.content)

with open('huozhuo.jpg', 'wb') as wbf:
    wbf.write(response.content)