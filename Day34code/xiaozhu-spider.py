"""
1、爬取小猪前3页房源数据（标题、地址、价格、封面图片、发布者昵称、发布者性别）并存储到 MongoDB 中
2、从 MongoDB 中筛选房价大于500元的房源
"""

import requests
from bs4 import BeautifulSoup
import pymongo
import time

# 获取前3页待爬去的URL
urls = ["http://bj.xiaozhu.com/search-duanzufang-p{}-0/".format(i) for i in range(1, 4)]


# print(urls)

# 链接MongoDB数据库
client = pymongo.MongoClient("127.0.0.1", 27017)

# 连接数据库
db = client.xiaozhu

# 指定集合
house_collection = db.house


def get_links(urls):
    """
    作用：获取所有的房源详情页url链接
    :param urls: 待爬取的URL列表
    :return: data 详情页的url列表
    """
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.89 Safari/537.36"
    }
    data = []
    for url in urls:
        response = requests.get(url, headers=headers)
        # response.encoding = response.apparent_encoding
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        links = soup.select("ul li a.resule_img_a")

        for i in range(len(links)):
            data.append(links[i].get('href'))

    return data


def get_one_data(url):
    """
    作用：爬取一个详情页的数据，并直接存储到MongoDB数据库中
    :param url: 详情页的URL
    :return:
    """

    print("正在爬取：{}".format(url))
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.89 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    title = soup.select("div.pho_info h4 em")[0].text.strip()
    address = soup.select("div.pho_info p")[0].get('title')
    price = soup.select("div.day_l span")[0].text
    member_name = soup.select("div.w_240 h6 a")[0].text
    member_sex_list = soup.select("div.member_pic div")[0].get('class')
    member_sex = member_sex_list[0] if len(member_sex_list) > 0 else ""

    data = {
        "title": title,
        "address": address,
        "price": price,
        "member_name": member_name,
        "member_sex": print_sex(member_sex)
    }
    house_collection.insert_one(data)


def print_sex(class_name):
    if class_name == "member_ico":
        return "男"
    elif class_name == "member_ico1":
        return "女"


if __name__ == '__main__':
    links = get_links(urls)
    # print(len(links))
    # print(links)
    for link in links:
        get_one_data(link)
        time.sleep(2)

    print("数据全部爬取完成！")