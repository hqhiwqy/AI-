# 3、定义一个getMax函数，返回三个数（从键盘输入的整数）中的最大值。


def getMax(a, b, c):
    t = 0
    if a > b:
        t = a
    else:
        t = b
    if t > c:
        return "最大值为：" + str(t)
    else:
        return "最大值为：" + str(c)


n1 = int(input('请输入第一个整数'))
n2 = int(input('请输入第二个整数'))
n3 = int(input('请输入第三个整数'))

max = getMax(a=n1, b=n2, c=n3)
print(max)
