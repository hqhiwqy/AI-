# Python其他语句

# break

print(list(range(5)))  # [0, 1, 2, 3, 4]

print(list(range(1, 5)))  # [1, 2, 3, 4]

for i in range(5):
    print('-----------------------')
    print(i)

for i in range(5):
    print('-----------------------')
    if i == 3:
        break
    print(i)

# continue : 结束当前循环，执行下次循环

for i in range(5):
    print('-----------------------')
    if i == 3:
        continue
    print(i)

# 注意：
# break/continue 语句只能在循环中使用，不能单独使用
# break/continue 语句用于嵌套循环，只对最近的一层循环起作用

# pass 空语句，作用为了保持程序结构的完整性，pass不做任何事情，一般用做占语句

if True:
    pass
    print('执行pass语句')
else:
    pass
print('执行结束')

# else

count = 0
while count < 5:
    print(count, '小于5')
    count += 1
else:
    print(count, '不小于5')