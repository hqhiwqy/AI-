# 元组   不可变 无增删操作

tuple1 = ()  # 空元组

print(tuple1, type(tuple1))  # () <class 'tuple'>

tuple2 = (1, 2, 3, 4)

print(tuple2, type(tuple2))  # (1, 2, 3, 4) <class 'tuple'>

tuple3 = (1)  # 只有1个元素，这种情况下，按小括号进行计算，最后结果就是1

print(tuple3, type(tuple3))  # 1 <class 'int'>

# 只有1个元素的元组我们定义的时候必须添加一个逗号来清除

tuple4 = (1,)

print(tuple4, type(tuple4))  # (1,) <class 'tuple'>

# 定义元组（至少有1个元素）的时候可以省略小括号

tuple5 = 1, 2
print(tuple5, type(tuple5))  # (1, 2) <class 'tuple'>

# 元组的相关操作

number_tuple = ('a', 'b', 'c')

print(number_tuple[1])  # b

print(number_tuple[::-1])  # ('c', 'b', 'a')

for temp in number_tuple:
    print(temp)

# + 操作

a = (1, 2)
b = (3, 4)

c = a + b
d = b + a
print(c)  # (1, 2, 3, 4)
print(d)  # (3, 4, 1, 2)

num_list = [1, 2, 3, 4, 5]

num_tuple = tuple(num_list)

print(num_tuple)