from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once a time there were three little sisters; and their names were
<a href="https://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="https://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="https://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">The Dormouse's story2</p>

</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# 通过标签名称查找
title_list = soup.select('title')
print(title_list)

for title in title_list:
    print(title, type(title), title.get_text())


# 通过类名查找
sister_list = soup.select('.sister')
print(sister_list)

for sister in sister_list:
    print(sister.get_text())


# 通过id名查找
link1 = soup.select('#link1')
print(link1)

link = soup.select('#link2,#link3')
print(link)

# 通过组合方式查找
title = soup.select('.title b')
print(title)

# 通过属性方式查找
elsie = soup.select('a[href="https://example.com/lacie"]')
print(elsie)