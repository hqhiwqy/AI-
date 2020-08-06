# selenuim + Chrome Headless 模式

import time

from selenium import webdriver

# 引入chrome选项

from selenium.webdriver.chrome.options import Options

# 配置chrome浏览器(无头模式)

chrome_options = Options()

chrome_options.add_argument('--headless')

chrome_driver = "D:/AI/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)

url = "https://my.cnki.net/Register/CommonRegister.aspx"

# 通过webdriver.PhantomJS方法传入phantomjs可执行程序文件所在的路径
# driver = webdriver.PhantomJS(executable_path="/Users/stark/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs")

# 访问网页内容
driver.get(url)

# driver.save_screenshot("zhiwang.png")


def get_code_img(filename):
    checkcode = driver.find_element_by_id("checkcode")

    # print(checkcode)

    save_img_path = "./images/{}.png".format(filename)

    # 局部截图
    checkcode.screenshot(save_img_path)

    checkcode.click()

    time.sleep(1)

    # checkcode_url = driver.find_element_by_id("checkcode").get_attribute('src')
    #
    # driver.get(checkcode_url)
    #
    # save_img_path = "./images/{}.png".format(filename)
    #
    # # 全局截图
    # driver.save_screenshot(save_img_path)


if __name__ == "__main__":
    for i in range(20):
        get_code_img(i+1)

