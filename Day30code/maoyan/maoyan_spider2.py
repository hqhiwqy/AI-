# 爬虫实战：运用正则表达式爬取猫眼电影排行
import requests
import re
import time
import csv

"""
爬取网站：https://maoyan.com/board/4
爬取内容：排名（ranks），电影名称（name），演员（actor），上映时间（year），评分（score）,国家（country）
爬虫思路：
    1、使用 requests 库 get 请求爬取相关信息，设置请求头，防止被墙；
    2、使用 re 库对爬取的数据进行筛选（主要使用 findall 方法，并添加 re.S 修饰符）；
    3、对筛选的数据进行 csv 存储；
    4、为防止被墙，每爬取一次休息 2s；
    5、由于是多页，找 url 规律并使用循环爬取。
"""


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


def get_info(url):
    """
    作用: 网页解析并保存到本地
    :param url: 请求的url
    """
    html = get_html(url, headers=headers)

    # 电影排名
    ranks = re.findall(r'<i class="board-index board-index-.*?">(.*?)</i>', html, re.S)
    # 电影名称
    names = re.findall(r'<p class="name"><a href="/films/.*?" title="(.*?)"', html, re.S)
    # 电影评分
    scores = re.findall(r'<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>', html, re.S)
    # 电影主演
    actors = re.findall(r'<p class="star">.*?主演：(.*?)</p>', html, re.S)
    # 上映时间
    years = re.findall(r'<p class="releasetime">上映时间：(.*?)</p>', html, re.S)
    # print(ranks)
    # print(names)
    # print(scores)
    # print(actors)
    # print(years)

    for rank, name, score, actor, year in zip(ranks, names, scores, actors, years):
       # print(rank, name, score, actor, year)
       writer.writerow([int(rank), name, actor.strip(), year, score[0] + score[1]])


if __name__ == "__main__":

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    urls = ["https://maoyan.com/board/4?offset={}".format(i) for i in range(0, 20, 10)]
    # print(urls)

    with open('./data/maoyan-top100-2.csv', 'a', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Rank', 'Name', 'Actor', 'Year', 'Score'])
        for url in urls:
            print('正在爬取：{}'.format(url))
            get_info(url)
            # 暂停2s
            time.sleep(2)
        print('数据全部下载成功！')