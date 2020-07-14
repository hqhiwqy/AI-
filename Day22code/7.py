# 匿名函数

square = lambda x: x ** 2

cube = lambda x: x ** 3

print(cube(3))

print(square(3))


# 普通函数

def squre(x):

    return x ** 2


print(square(5))

# • 普通函数使用 def 关键字，而匿名函数使用 lambda 关键字。
# • 普通函数是有名称的，而匿名函数没有名称。
# • 普通函数的函数体中可以包含多条语句，而匿名函数的函数体只有一个表达式。
# • 普通函数的函数体中可以使用 if、for 等语句，而匿名函数中不可以使用。
# • 普通函数一般用于实现复杂的功能，而匿名函数只能实现简单的功能。
# • 普通函数可以被其它程序调用，而匿名函数不能共享给其它程序使用。

list1 = [(lambda x: x*x)(i) for i in range(10)]

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(list1)

list2 = [(1, 20), (3, 0), (10, 9), (2, -1)]

list2.sort(key=lambda x: x[1])  # 按照列表中元组的第2个元素进行排序  升序排列

print(list2)

list2.sort(key=lambda x: x[1], reverse=True)  # 按照列表中元组的第2个元素进行排序  降序排列

print(list2)