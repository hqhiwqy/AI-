from urllib.error import HTTPError

import requests
from bs4 import BeautifulSoup


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
        # 如果 HTTP 请求返回了不成功的状态码 Response.raise_for_status() 会抛出一个HTTPError 异常。
        response.raise_for_status()

        return response.text
    except HTTPError as err:
        return err
    except Exception as err:
        return err


def parse_html(html):
    """
    作用：网页解析
    :param html:网页内容
    :return data:有价值的数据
    """
    pass


def save_file(data):
    """
    数据存储
    :param data:
    :return:
    """
    pass


def main():
    # 1.爬取网页
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    urls = ["https://movie.douban.com/top250?start={}&filter=".format(i) for i in range(0, 225, 25)]
    # print(urls)
    html = get_html(urls, headers=headers)
    # 2.网页解析
    data = parse_html(html)
    # print(data)
    # 3.保存数据
    save_file(data)


if __name__ == '__main__':
    main()
