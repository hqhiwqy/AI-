#  find
#  find 函数用于检测字符串中是否包含子字符串 sub，如果指定 start
# （开始）和 end （结束）范围，则检查是否包含在指定范围内。如果包含子字符串则返回开始的索引值，否则返回-1。 •
#  语法格式如下：
# • str.find(sub[, start[, end]])
# • 参数含义如下：
# • sub：指定检索的字符串
# • start：开始索引，默认为0 • end：结束索引，默认为字符串长度

lang = "Python"
print(lang.find('on'))

# index函数和find类似，区别就是如果找不到抛出异常
print(lang.index('Py'))
# print(lang.index('ok'))  # 抛出异常

# count
# count 函数用于统计字符串中 sub 子串出现的次数，可以设定开始与结束位置来限制字符串的搜索范围。
# • 语法格式如下：
# • str.count(sub[, start[, end]])
# • 参数含义如下：
# • sub：搜索的子字符串
# • start：字符串开始搜索的位置，默认为第一个字符，该字符索引值为0 • end：字符串结束搜索的位置，默认为字符串的长度

langs = "html, css, js, go, c, python, java, python"

print(langs.count('python'))


# replace
# • replace 函数把字符串中的 old （旧字符串）替换成（新字符串），
# 该函数返回的是字符串中 old （旧字符串）替换成 new (新字符串)
# 后生成的新字符串。如果指定第3个参数 count ，则替换不超过
# count 次。
# • 语法格式如下：
# • str.replace(old, new[, count]])
# • 参数含义如下：
# • old：将被替换的子字符串
# • new：新字符串，用于替换 old 子字符串
# • count：可选参数，替换不超过 count 次


new_langs = langs.replace('python', 'Python')

print(new_langs)

new_langs = langs.replace('python', 'Python', 1)

print(new_langs)

# split
# split 函数通过指定分隔符对字符串进行切片
# 如果参数 maxsplit有指定值，则仅分隔 maxsplit 个子字符串。
# 该函数返回值是分隔后的字符串列表。

print(langs.split())
print(langs.split(',', 1))

# startswith 函数用于检查字符串是否是以子字符串开头，
# 如果是，则返回 True，否则返回 False。
print(langs.startswith('html'))

# endswith 函数用于判断字符串是否以指定后缀结尾，
# 如果以指定后缀结尾返回 True，否则返回 False。
print(langs.endswith('js'))

# 字符串运算符
# + 字符串连接
# * 重复输出字符串
print('-'*10)
# in 如果字符串中包含给定的字符，返回True，否则返回False
# not in 如果字符串中不包含给定的字符，返回True，否则返回False