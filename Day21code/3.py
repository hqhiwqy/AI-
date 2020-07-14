# 列表

list1 = list([1, 2, 3, 4])
print(list1, type(list1))  # <class 'list'>

list2 = [1, 2, 3, 4]
print(list2, type(list2))  # <class 'list'>

list3 = ['1', 'hello', True, 4.5]
print(list3, type(list3))  # <class 'list'>

import timeit

print(timeit.timeit('l1 = list()'))
print(timeit.timeit('l2 = []'))

# 列表切片

# 切片语法： 列表变量名[开始：结束：步长]

list4 = ['a', 'b', 'c', 'd', 'e', 'f']

print(list4[0])  # 返回列表的下标为0的元素
print(list4[3])  # 返回列表的下标为3的元素
print(list4[len(list4) - 1])  # 返回列表最后一个元素
print(list4[-1])  # 返回列表倒数第一个位置的元素
# print(list4[6])  # IndexError: list index out of range

print(list4[::2])
print(list4[::-2])
print(list4[-2:-1])
print(list4[-2:1])

# 列表的遍历

num_list = [1, 3434, 45, 656, 2, 98, 3]

# 计算列表中所有元素的和

sum = 0
for i in num_list:
    sum += i
print(sum)

# 计算列表中所有偶数的和

sum = 0
for i in num_list:
    if i % 2 == 0:
        sum += i
print(sum)

name_list = ['张三', '李四', '王五']

temp_name = input('请输入要添加的学生姓名：')

# 列表中添加
# append——向列表添加元素，在末尾添加
name_list.append(temp_name)

print(name_list)

# extend——将一个列表中的元素全部添加到另外一个列表
list_one = [1, 2]
list_two = [3, 4]

list_one.extend(list_two)
print(list_one)
list_two.extend(list_one)
print(list_two)

# insert——可以在列表的指定位置添加元素
list_one = [1, 2]
list_one.insert(5, 3)  # 索引超过列表最大的范围，会在最后添加
print(list_one)
list_one.insert(1, [4, 5])
print(list_one)

list_two = ['a', 'b', 'd']
print(list_two)
list_two[2] = 'c'
print(list_two)
# list_two[3] = 'f'  # IndexError: list index out of range

# 删除
# del:根据下标进行删除
# pop:删除最后一个元素
# remove: 根据元素的值进行删除
list_three = ['a', 'b', 'c', 'd', 'e', 'f']

del list_three[2]
print(list_three)

list_three.pop()
print(list_three)

list_three.remove('b')
print(list_three)

# 排序
# sort
# reverse

num_list = [1, 4, 6, 3, 9]
num_list.reverse()  # 降序排列
print(num_list)

num_list.sort()     # 升序排列
print(num_list)

num_list.sort(reverse=True)  # 降序排列
print(num_list)

# 列表的嵌套
# 案例一：分配教师给不同的办公室
# 描述：已知某学校由3个办公室和8名教师，请编写一个程序，完成教师和办公室的随机分配

import random  # 随机数
# 定义一个列表offices用来保存3个办公室，编号分别为1，2，3
offices = [[], [], []]   # 办公室初始为空列表，表示没有分配老师

# 定义一个列表names来保存8位老师的名字
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# 遍历names列表，取出每个老师的名字，之后随机选取一个办公室，将老师的名字添加到办公室
for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)
i = 1
# 查看随机分配的结果
for temp in offices:
    print('办公室{}的人数位：{}'.format(i, len(temp)))
    i += 1
    for name in temp:
        print('{}'.format(name), end=" ")
    print()