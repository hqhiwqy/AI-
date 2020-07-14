# 2、请设计一个函数随机生成指定长度的验证码（验证码由大小写字母和数字构成）。


import random


def random_num(n):
    x = 0
    while x < n:
        s = random.choice(range(1, 4))
        if s == 1:
            a = random.choice(range(1, 10))
            print(a, end='')
            x += 1
        if s == 2:
            b = random.choice(range(69, 90))
            print(chr(b), end='')
            x += 1
        if s == 3:
            c = random.choice(range(97, 122))
            print(chr(c), end='')
            x += 1


n = int(input('请输入验证码个数：'))

random_num(n)
