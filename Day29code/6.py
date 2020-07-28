# 使用 requests 模拟浏览器发送 POST 请求

import requests


def get_html(url, params=None, headers=None, method='GET'):
    """
    作用：爬虫爬取网页
    :param url: 爬取目标网页
    :param method: 请求方式，默认get方式
    :param params: 请求参数
    :param headers: 请求报头
    :return: 网页内容
    """
    try:
        if method == 'get' or method == 'GET':
            response = requests.get(url, params=params, headers=headers)
        elif method == 'post' or method == 'POST':
            response = requests.post(url, params=params, headers=headers)

        response.encoding = response.apparent_encoding
        return response.text
    except Exception as err:
        print(err)


if __name__ == '__main__':

    word = input('请输入需要翻译的文字：')

    url = "http://m.youdao.com/translate"

    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 "
                      "(KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }

    formdata = {
        "inputtext": "word",
        "type": "AUTO"
    }

    html = get_html(url, formdata, headers, 'POST')

    print(html)