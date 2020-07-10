# 变量的类型

# 数字类型

a = 10

print(type(a))  # <class 'int'>

a = 3.14

print(type(a))  # <class 'float'>

# 布尔类型：True、False

print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>

# 字符串类型

print(type('HQH'))   # <class 'str'>
print(type("HQH"))   # <class 'str'>
print(type('8'))     # <class 'str'>
print(type('True'))  # <class 'str'>

# 空值 None

# 空值是Python中一个特殊的值，用None表示（注意N大写），None不能理解为0，因为0是有意义的，None是一个特殊的空值

print(type(None))  # <class 'NoneType'>

# 列表（list）是一个可以放置任意数据类型的可变有序集合

name_list = ['zhangsan', 'zs', '张三']

print(type(name_list))  # <class 'list'>

# 元组（tuple）和list类似，但是元组一旦初始化了就不可变，即不支持添加，修改，删除等操作

tuple = (1, 2, 3, 4)

print(type(tuple))  # <class 'tuple'>

# 集合(set)是一系列、不重复的元素的组合，和字典类似，但集合没有键和值的配对，即只有一组key的集合，但没有value。

s1 = {1, 2, 3}
print(type(s1))  # <class 'set'>

# 字典(dict)

d1 = {'name': 'cc', 'age': 18}

print(type(d1))  # <class 'dict'>