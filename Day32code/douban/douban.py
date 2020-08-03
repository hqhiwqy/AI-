from selenium import webdriver
import time
# 通过webdriver.PhantomJS方法传入phantomjs可执行程序文件所在的路径
driver = webdriver.PhantomJS(executable_path="D:/AI/phantomjs-2.1.1-windows/bin/phantomjs.exe")

# 获取豆瓣网页内容
driver.get("https://www.douban.com")

# 切换到登录框iframe中
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

# 鼠标单击切换到密码登录
driver.find_element_by_class_name("account-tab-account").click()

# 定位到id=username的页面元素，并输入手机号\邮箱
driver.find_element_by_id("username").send_keys("16603584018")

# 定位到id=password的页面元素，并输入密码
driver.find_element_by_id("password").send_keys("hao7883370")

# 定位到class-btn-account的登录按钮元素，并进行鼠标点击操作
driver.find_element_by_class_name("btn-account").click()

time.sleep(3)

driver.save_screenshot("douban.png")