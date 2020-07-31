# 使用 bs4 的基本原理

# 安装 bs4 库

# pip install beautifulsoup4 -i https://pypi.tuna.tsinghua.edu.cn/simple

# 导入 bs4 库

from bs4 import BeautifulSoup
import re
html = """
    <html>
        <head>
            <title>爬虫测试页面</title>
        </head>
        <body>
            <a href="https://www.baidu.com" class="baidu_link">百度</a>
            <a href="https://www.zhihu.com" class="zhihu_link">知乎</a>
            <a href="https://www.douban.com" class="douban_link">豆瓣</a>
        </body>
    </html>
"""
# 1.创建Beautiful Soup类对象
soup = BeautifulSoup(html, "html.parser")  # html.parser指的是HTML解析器

# 查找所有的a标签
a_list = soup.find_all('a')
print(a_list)

for a in a_list:
    print(a)

# 根据url值查找a标签
baidu_node = soup.find('a', href="https://www.baidu.com")
print(baidu_node)
print(baidu_node.name)  # 节点名称
print(baidu_node.get('href'))  # 获取节点的href属性值
print(baidu_node.get_text())  # 获取节点的文本

# 根据class查找a标签
zhihu_node = soup.find('a', class_='zhihu_link')
print(zhihu_node)
print(zhihu_node.name)  # 节点名称
print(zhihu_node.get('href'))  # 获取节点的href属性值
print(zhihu_node.get_text())  # 获取节点的文本

# 模糊查找
douban_node = soup.find('a', href=re.compile('ban'))
print(douban_node)
print(douban_node.name)  # 节点名称
print(douban_node.get('href'))  # 获取节点的href属性值
print(douban_node.get_text())  # 获取节点的文本