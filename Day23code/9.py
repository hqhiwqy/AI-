# 读取json

import json

userinfo = {
    "name": "张三",
    "age": 28,
    "QQ": 12345678,
    "firends": ["李四","王五"],
    "cars":[
        {
            "brand":"BYD","max_spedd": 180,
            "brand":"Audi","max_spedd":200
        }
    ]
}

f = open('./data/userinfo.json', 'w', encoding='utf-8')

json.dump(userinfo, f)

f.close()

print('保存数据成功！')