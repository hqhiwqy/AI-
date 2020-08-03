class UrlManager:
    """url管理器"""

    def __init__(self):
        self.new_urls = set()  # 待爬取的url集合
        self.old_urls = set()  # 已爬取的url集合

    def add_new_url(self, url):
        """
        作用：添加一个url到待爬取的url集合中
        :param url: 一个新的url
        """
        if url is None:
            return

        # 防止重复爬取和循环爬取
        if url is not self.new_urls and url is not self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        作用：批量添加url
        :param urls: url列表
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        """
        作用：判断是否有新的待爬取的url
        :return: 返回True  False
        """
        return len(self.new_urls) != 0

    def get_new_url(self):
        """
        作用：获取一个新的待爬的url
        :return: new_url
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
