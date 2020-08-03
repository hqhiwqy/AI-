from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchAttributeException
import time

# 通过webdriver.PhantomJS方法传入phantomjs可执行程序文件所在的路径
driver = webdriver.PhantomJS(executable_path="D:/AI/phantomjs-2.1.1-windows/bin/phantomjs.exe")

# 获取网页内容
driver.get("https://www.baidu.com")

# 打印页面源码
# print(diver.page_source)

# 打印页面的标题
print(driver.title)
driver.save_screenshot("打开.png")

# 获取id=kw的元素,并且输入搜索内容
driver.find_element_by_id("kw").send_keys(u"中国")
# 模拟键盘Enter
driver.find_element_by_id("kw").send_keys(Keys.RETURN)
time.sleep(2)

# 生成当前页面，并且页面截屏保存
driver.save_screenshot("中国.png")

print(driver.page_source)

# 关闭当前页面
driver.close()
# diver.save_screenshot("关闭.png")
# 直接关闭浏览器
driver.quit()