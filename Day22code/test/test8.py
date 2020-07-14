# 8、编写函数，求两个正整数的最小公倍数。
import math


def min():
    a = int(input("请输入第一个数："))
    b = int(input("请输入第二个数："))
    # 交换位置,大的在后,小的在前
    if a > b:
        a, b = b, a
    # 穷举法寻找公约数
    for n in range(1, a + 1):
        if a % n == 0 and b % n == 0:
            gys = n
    # 最小公倍数:两个数相乘除以公约数
    mingbs = (a * b) / gys
    print(f'你输入的数是：{a},{b}')
    print(f'这两个数的最小公倍数是：{mingbs}')


min()
