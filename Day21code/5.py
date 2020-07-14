# 字典

dict1 = {'name': 'caocao', 'age': 18}
dict2 = dict({'name': 'caocao', 'age': 18})
dict3 = dict([('name', 'caocao'), ('age', 18)])
dict4 = dict(name="caocao", age=18)
print(dict1, dict2, dict3, dict4)
print(dict1 == dict2 == dict3 == dict4)

# 空字典

dict5 = {}
dict6 = dict()

print(dict5, dict6)

# 当键（key）重复时，字典如何处理？
dict7 = {'a': 'aaaa', 'b': 'bbbb', 'a': 'cccc'}
print(dict7)

# 字典常见的操作

dict8 = {'name': 'cao', 'age': 22, 'sex': '男'}
print(dict8['name'], dict8['sex'], dict8['age'])

dict8['age'] = '24'
print(dict8['name'], dict8['sex'], dict8['age'])

dict8['city'] = '孝义'
print(dict8['name'], dict8['sex'], dict8['age'], dict8['city'])

dict8.pop('age')
print(dict8)

dict8.clear()  # 清空字典
print(dict8)


# 字典的遍历
# 遍历字典的键
dict9 = {'name': 'cao', 'age': 22, 'sex': '男'}
for key in dict9.keys():
    print(key)

# 遍历字典的值
for value in dict9.values():
    print(value)

# 遍历字典的元素
for item in dict9.items():
    print(item)  # 元组

# 遍历字典的键值对
for key, value in dict9.items():
    print(key, value)