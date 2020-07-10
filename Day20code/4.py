# 运算符

# 2的10次方

print(2**10)

list1 = [1, 2, 3, 4]

a = 10
b = 20

if a in list1:
    print('变量a在list1中')
else:
    print('变量a不在list1中')

if b not in list1:
    print('变量b不在list1中')
else:
    print('变量b在list1中')

# 比较聊个变量均为可变的类型

list2 = [1, 2]

list3 = [3, 4]

print(list2 is list3)  # Flase

print(list2 == list3)  # Flase

print(id(list2) == id(list3))  # Flase

# 比较的两个变量均为不可变的类型

str1 = 'hello'
str2 = 'hello'
print(str1 is str2, id(str1) == id(str2), str1 == str2)  # True True True
