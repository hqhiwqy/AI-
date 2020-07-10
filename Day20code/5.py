# 例1：  如果年龄大于18岁，输出已成年

age = 20

if age >= 18:
    print('已成年')

# 例2： 如果年龄大于18岁，输出已成年，如果年龄不满18岁，输出未成年。

if age >= 18:
    print('已成年')
else:
    print('未成年')

# 例3： 判断输入的数是奇数还是偶数

number = input('请输入一个数：')

# number = int(input('请输入一个数：'))  # 由于input返回的数据类型是str，必须先把str转换成整数

print(number, type(number))  # <class 'str'> 字符串类型

if int(number) % 2 == 0:  # int 进行类型转换
    print('偶数')
else:
    print('奇数')

# 例4: 判断今天是星期几？

import time

local_time = time.localtime()  # 返回当前时间

w = time.strftime('%w', local_time)

print(w, type(w))

if w == '1':
    print('今天是星期一')
elif w == '2':
    print('今天是星期二')
elif w == '3':
    print('今天是星期三')
elif w == '4':
    print('今天是星期四')
elif w == '5':
    print('今天是星期五')
elif w == '6':
    print('今天是星期六')
else:
    print('今天是星期天')

# Python中没有switch语句

# 例5： 判断输入的数是否整除2和3？

number = int(input('请输入一个数：'))

if number % 2 == 0:
    if number % 3 == 0:
        print('输入的数字可以整除2和3')
    else:
        print('输入的数字可以整除2但不能整除3')
else:
    if number % 3 == 0:
        print('输入的数字可以整除3但不能整除2')
    else:
        print('输入的数字不可以整除2也不能整除3')

# 例6：计算100以内所有奇数的和

sum = 0
n = 99
while n > 0:
    sum += n
    n = n - 2
print(sum)

# 例7：数字猜谜游戏

result = 8
guess = -1

print('数字猜谜游戏正式开始！')

while guess != result:
    guess = int(input('请输入你猜的数字：'))
    if guess < result:
        print('很遗憾，你猜的数字小了')
    elif guess > result:
        print('很遗憾，你猜的数字大了')
    else:
        print('恭喜你，猜对了！')

# Python中没有do while循环

# for 循环

# 语法格式

# for 临时变量 in 序列：
# 循环体

# 例8：使用for循环来计算1-10的总和
sum = 0

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += i
print(sum)

# 例9：使用for循环来计算1-100的总和

# range(start, stop[,step])-根据指定的开始位置，结束位置，以及步长，生成数字队列

list1 = range(0, 101)  # range(0, 101)
print(list1, type(list1))  # <class 'range'>

list2 = range(0, 101, 10)  # range(0, 101)
print(list2, type(list2))  # <class 'range'>

print(list(list1))
print(list(list2))
sum = 0
for i in list1:
    sum += i
print(sum)