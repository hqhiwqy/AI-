# 函数式编程常见的内置函数

list1 = [1, 2, 3, 4]

# 此时test函数并不是一个纯函数


def test1(l):
    for index in range(0, len(l)):
        l[index] *= 2
    return l


print(test1(list1), list1)

# map()—— 根据提供的函数对指定的序列做映射

list1 = [1, 2, 3, 4]

new_list = list(map(lambda x: x * 2, list1))

print(new_list, list1)

# filter() ——根据提供的函数对指定的序列执行过滤操作

list2 = [1, 2, 3, 4, 5]

new_list2 = list(filter(lambda x: x % 2 == 0, list2))

print(new_list2, list2)

# functools.reduce() ——根据提供的函数对指定的序列中的元素进行累积

from functools import reduce

print(reduce(lambda x, y: x * y, list2))

