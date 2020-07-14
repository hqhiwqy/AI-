# 1、编写一个程序，实现删除列表重复元素的功能。
list1 = [1, 2, 2, 4, 1, 5, 7]

# 使用字典函数fromkeys()

dict1 = dict.fromkeys(list1)

print(dict1)

list2 = list(dict1.keys())

print((list2))

# 使用集合set函数

list3 = list(set(list1))
print(list3)

# 2、假设有两个3x3矩阵，编写一个程序，计算这两个矩阵的和并输出。

matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# 解法1

matrix_result = [[None] * 3 for _i in range(3)]

# [[None, None, None], [None, None, None], [None, None, None]]

print(matrix_result)

for i in range(len(matrix_a)):
    for j in range(len(matrix_b)):
        matrix_result[i][j] = matrix_a[i][j] + matrix_b[i][j]
print(matrix_result)

# 解法2


# 3.编写一个程序，使用字典保存学生的信息：学号和姓名，将学生的信息按照从小到大排序，排序后进行输出。

# sort函数和sorted函数的区别
# 1.sort是应用在list上的方法，而sorted可以对所有可迭代的对象进行排序操作
# 2.sort返回的是对已经存在列表进行的操作，而sorted返回的是一个新的

list4 = [2, 4, 6, 1, 8, 10]
list5 = sorted(list4)
print(list5, list4)

students = [('张三', '男', 18), ('李四', '男', 10), ('王五', '女', 25)]

# 按年龄排序（从小到大）
students_result1 = sorted(students, key=lambda x: x[2])

print(students_result1)

# 按年龄排序（从大到小）
students_result2 = sorted(students, key=lambda x: x[2], reverse=True)

print(students_result2)


# 4.已知一个列表存储多个整数，请编写一个函数，删除列表中的质数

def filter_prime_number(arg):
    result = []
    for item in arg:
        for i in range(2, item):
            if item % i == 0:
                result.append(item)
                break
    return result


list6 = [2, 3, 6, 3, 1, 8]

result = filter_prime_number(list6)

print(result)
