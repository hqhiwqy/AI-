# 4、打开一个英文文本文件，编写程序读取其内容，并把其中的大写字母变成小写字母，小写字母变成大写字母。

# 字符串函数——swapcase() 对字符串的大小写进行转换


f = open('../data/in.txt', 'r')
content = f.read()
new_content = content.swapcase()
print(new_content)
f.close()