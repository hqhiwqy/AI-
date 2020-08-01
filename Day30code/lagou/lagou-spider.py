import json

import jsonpath
import requests


# 1.爬取网页


def get_html(url, params=None, headers=None, method='GET'):
    """
    作用：爬虫爬取网页
    :param url: 爬取目标网页
    :param headers: 请求报头
    :param params: 请求参数
    :param method: 请求方式，默认get方式
    :return: 网页内容
    """

    try:
        if method == 'get' or method == 'GET':
            response = requests.get(url, params=params, headers=headers)
        elif method == 'post' or method == 'POST':
            response = requests.post(url, data=params, headers=headers)

        if response.apparent_encoding != "Windows-1254":
            response.encoding = response.apparent_encoding

        return response.text
    except Exception as err:
        return err


if __name__ == '__main__':
    url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    json_citys = get_html(url, headers=headers)
    # print(json_citys)

    # 将json字符串转换成Python对象
    json_citys_obj = json.loads(json_citys)
    # print(json_citys_obj)

    # 不管位置，选取所有根节点下所有的name节点，其中 $ 表示根节点，..表示不管位置
    city_list = jsonpath.jsonpath(json_citys_obj, '$..name')
    # print(city_list)

    # 将列表序列化成一个json字符串,设置参数ensure_ascii=False来禁用ASCII编码
    city_json = json.dumps(city_list, ensure_ascii=False)

    # 将json字符串保存到文件中
    with open('city.json', 'w') as file:
        file.write(city_json)