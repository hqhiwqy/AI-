# 4、编写函数，求出 1/(1x2)-1/(2x3)+1/(3x4)-1/(4x5)+… 前n项的和，函数以n为参数，它是用户输入的。


def sum(n):
    """
    求出 1/(1x2)-1/(2x3)+1/(3x4)-1/(4x5)+… 前n项的和
    :param n: 整数
    :return:  r: 计算结果
    """
    r = 0
    while n >= 1:
        if n % 2 == 0:
            r -= 1/(n * (n+1))
        else:
            r += 1/(n * (n+1))
        n -= 1
    return r


num = int(input("请输入一个整数："))

print(sum(num))
