from selenium import webdriver

# 通过webdriver.PhantomJS方法传入phantomjs可执行程序文件所在的路径
driver = webdriver.PhantomJS(executable_path="D:/AI/phantomjs-2.1.1-windows/bin/phantomjs.exe")

# 获取网页内容
driver.get("https://www.baidu.com")

# css选择器定位一个元素
hot_title = driver.find_element_by_css_selector("div.s-hotsearch-title a.hot-title div.title-text").text
print(hot_title)

# css选择器定位多个元素
hot_search = driver.find_elements_by_css_selector("ul.s-hotsearch-content li.hotsearch-item")
# print(hot_search)


for item in hot_search:
    print(item.text)