import re

from bs4 import BeautifulSoup
from urllib.parse import urljoin

# pip install beautifulsoup4 -i https://pypi.tuna.tsinghua.edu.cn/simple


class HtmlParser:
    """网页解析器"""

    def parse(self, html_text, page_url):
        """
        作用：解析网页内容
        :param html_text:需要解析的网页内容
        :param page_url: 网页url
        :return:new_data, new_urls
        """
        if html_text is None:
            return
        soup = BeautifulSoup(html_text, "html.parser")
        new_data = self._get_new_data(soup, page_url)
        new_urls = self._get_new_urls(soup, page_url)

        return new_data, new_urls

    def _get_new_data(self, soup, page_url):
        """
        作用：解析有效数据
        :param soup:
        :param page_url:
        :return: data
        """
        data = dict()
        data['title'] = soup.select("dd.lemmaWgt-lemmaTitle-title h1")[0].text
        data['summary'] = soup.select("div.lemma-summary .para")[0].text
        data['url'] = page_url
        return data

    def _get_new_urls(self, soup, page_url):
        """
        作用：解析新的URL地址
        :param soup:
        :return:
        """
        urls = soup.find_all("a", href=re.compile(r'/item/.*?/\d?'))
        new_urls = []
        for url in urls:
            href = url['href']
            full_url = urljoin(page_url, href)
            new_urls.append(full_url)
        return new_urls