# 聚合数据笑话大全接口地址
import json

import requests

joke_url = "http://v.juhe.cn/joke/randJoke.php"

params = {'key': 'b10bbc3126e377305ed9ce63763be02d'}

response = requests.get(joke_url, params=params)

# print(response.text)

# print(type(response.text))    str

joke_data = json.loads(response.text)

print(joke_data)

joke_data_result = joke_data['result']

for i in range(len(joke_data_result)):
    print("{}, {}\n".format(i+1, joke_data_result[i]['content']))
