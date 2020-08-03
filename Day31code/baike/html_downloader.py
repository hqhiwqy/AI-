import requests

# pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple


class HtmlDownloader:
    """网页下载器 """
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }

    def download(self, url):
        """

        :param url:需要下载的url
        :return:text
        """
        if url is None:
            return None
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
        except requests.HTTPError as e:
            print("HTTPError:{}".format(e))
        except Exception as e:
            print(e)
        else:
            return response.text