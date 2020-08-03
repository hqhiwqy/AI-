"""
爬虫实战：运用bs4爬取世界赛艇男运动员信息
• 爬取网站：2018年23岁以下世界赛艇锦标赛
• http://www.worldrowing.com/events/2018-world-rowing-under-23-championships/u23-mens-eight/
• 爬取内容：
    •  姓名（name）
    • 位置（position）
    • 图片链接（img_url）
    • 性别（sex）
    • 生日（birthday）
    • 国家（country
"""
import csv

from bs4 import BeautifulSoup
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


def parse_html(html):
    """
    作用：网页解析
    :param html:网页内容
    :return data:有价值的数据
    """
    soup = BeautifulSoup(html, 'html.parser')
    # players = soup.select("tr.resultsDetails li", limit=1)
    players = soup.select("tr.resultsDetails li")
    # print(players)
    print('一共有{}运动员'.format(len(players)))
    data = []
    for player in players:
        item = {}
        item['name'] = player.select("h4 a")[0].text
        item['position'] = player.select("p.yPadding")[0].text.strip()
        item['img_url'] = "http://www.worldrowing.com" + player.select("img.basicShadow")[0]['src']
        detail_url = "http://www.worldrowing.com" + player.select("h4 a")[0]['href']
        # 根据运动员详情页地址来爬取运动员详情页网页内容
        detail_html = get_html(detail_url)
        soup2 = BeautifulSoup(detail_html, "html.parser")
        item['sex'] = soup2.select("div.dd")[0].text
        item['birthday'] = soup2.select("div.dd")[1].text
        item['country'] = soup2.select("h1.athleteInfoTitle span")[0].text
        data.append(item)
    return data


def save_file(data):
    with open("world-rowing1.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Sex', 'Birthday', 'Country', 'Position', 'ImgUrl'])
        for item in data:
            writer.writerow([item['name'],
                             item['sex'],
                             item['birthday'],
                             item['country'],
                             item['position'],
                             item['img_url']])
        print("数据全部保存成功！")


def main():
    # 1.爬取网页
    url = "http://www.worldrowing.com/events/2018-world-rowing-under-23-championships/u23-mens-eight/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    html = get_html(url, headers=headers)
    # 2.网页解析
    data = parse_html(html)
    # print(data)
    # 3.保存数据
    save_file(data)


if __name__ == '__main__':
    main()
