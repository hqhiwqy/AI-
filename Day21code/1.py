# Python 字符串

name1 = 'caocao'

name2 = "lizi"

str1 = """
       hello
       world
       """
print(str1)

str2 = '''
       hello
       world
       '''
print(str2)


def demo():
    """
    :return:
    """


# 转义符

str3 = 'let \'s go!'
print(str3)

print('hello\nworld')

print(r'hello\world')  # 字符串前添加一个r，表示原始字符串

print('hello\\world')

print("My name is %s and weight is %d kg!" % ('caocao', 55))

# str.format() ——字符串格式化函数

print("My name is {} and weight is {} kg!".format('cc', 55))

name = input('请输入你的姓名：')
age = input('请输入你的年龄：')

print("姓名：{}, 年龄: {}".format(name, age))

# 访问字符串的值

# 切片是指对操作的对象截取其中一部分的操作
# 字符串、列表、元组都支持切片操作
# 切片的语法格式：[起始：结束：步长]
# 注意：包括开始位本身，不包含结束位本身

str = "abcdef"

print(str[0:3])   # 返回下标0-2的字符
print(str[3:5])   # 返回下标3、4的字符
print(str[1:-1])  # 返回下标为1开始到倒数第2个之间的字符
print(str[2:])    # 返回下标从2开始到最后
print(str[::-2])  # 倒序从后往前，中间隔两个取（步长为2）字符