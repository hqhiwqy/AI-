from baike.html_downloader import HtmlDownloader
from baike.html_outputer import HtmlOutputer
from baike.html_parser import HtmlParser
from baike.url_manager import UrlManager


class SpiderMain:
    """爬虫调度器"""

    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()

    def craw(self, url):
        """爬取网页"""
        self.urls.add_new_url(url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("正在爬取{}:{}".format(count, new_url))
                html_text = self.downloader.download(new_url)
                new_data, new_urls = self.parser.parse(html_text, new_url)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 20:
                    break
                count += 1
            except Exception as e:
                print("Craw Failed: {}".format(e))
        self.outputer.output_html()
        print("数据全部爬取成功！")


if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python/407313"
    baike_spider = SpiderMain()
    baike_spider.craw(root_url)
