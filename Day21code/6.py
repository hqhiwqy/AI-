# 集合

# 集合（set）和字典基本相同，唯一的区别，就是集合没有键和值的
# 配对（即集合也是一组 key 的集合，但不存储 value）。

# 集合是一系列无序的、不重复（唯一）的元素组合

set1 = {1, 2, 3}
set2 = set([1, 2, 3])

print(type(set1), type(set2))
print(set1 == set2)

# 集合不支持索引操作，因为集合本质上是一个哈希表

# print(set1[0])   TypeError: 'set' object is not subscriptable

set3 = set()
set4 = {}  # 空字典
print(type(set4))  # <class 'dict'> 空字典

# 集合常见的操作
# 添加 add
num_set = {'a', 'b', 'c'}
num_set.add('d')
print(num_set)  # 随机

# 删除 remove
num_set.remove('d')
print(num_set)

# 删除 discard
num_set.discard('a')
print(num_set)

# 删除 clear
# set5.clear()
# print(set5)    # set()  清除

# 更新 update update(序列)：把要传入的元素拆分，作为个体添加到集合中，同时对元素去重。

set5 = set('love')
print(set5)

set5.update('python')  # 自动去重
print(set5)

# set5.remove('python')  # KeyError: 'python'
# print(set5)

set5.add('python')  # 整体添加
print(set5)

set5.remove('python')
print(set5)

set5.discard('python')
print(set5)

set5.pop()  # 随机删除
print(set5)

# 一般集合常用符号

s1 = {1, 2, 3}
s2 = {1, 2, 3, 4}

print(s1 - s2)  # set()
print(s2 - s1)  # {4}  求差集

print(s1 & s2)  # {1, 2, 3} 求交集
print(s1 | s2)  # {1, 2, 3, 4} 并集

print(s1 <= s2)  # True  判断s1是否是s2的子集
