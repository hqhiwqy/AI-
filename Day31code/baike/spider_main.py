from baike import url_manager
import baike.html_downloader as html_downloader
import baike.html_parser as html_parser
import baike.html_outputer as html_outputer


class SpiderMain:
    """爬虫调度器"""

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

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
                if count == 10:
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
