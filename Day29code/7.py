# 案例：爬取百度贴吧


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
        # 当从内容中分析出的响应编码不是Windows-1254，才执行response.encoding = response.apparent_encoding
        if response.apparent_encoding != "Windows-1254":
            response.encoding = response.apparent_encoding
        return response.text
    except Exception as err:
        print(err)


def write_page(html, filename):
    """
    作用：将html内容写入本地的文件
    :param html: 网页内容
    :param filename: 保存的文件名
    :return:
    """
    print('正在保存' + filename)
    with open(filename, 'w', encoding='utf-8') as wf:
        wf.write(html)


def tieba_spider(url, begin_page, end_page):
    """
    作用：百度贴吧爬虫调度器
    :param url: 百度贴吧的前半部分（https://tieba.baidu.com/f）
    :param begin_page: 起始页码
    :param end_page: 结束页码
    """

    # page = 1, pn=0
    # page = 2, pn=50
    # page = 3, pn=100
    for page in range(begin_page, end_page + 1):
        pn = (page - 1) * 50
        file_name = "./data/" + str(page) + ".html"
        params = {
            "kw": kw,
            "pn": pn
        }
        html = get_html(url, params=params, headers=headers)
        write_page(html, file_name)

    print('Tieba Spider Success！')


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.97 Mobile Safari/537.36"
    }
    kw = input("请输入需要爬取的百度贴吧名：")
    begin_page = int(input("请输入起始页："))
    end_page = int(input("请输入结束页："))
    url = "https://tieba.baidu.com/f?kw=" + kw
    tieba_spider(url, begin_page, end_page)