# 解法二


def lcm(a, b):
    """
    求两个正整数的最小公倍数
    :param a: 正整数
    :param b: 正整数
    :return result: 最小公倍数
    """
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return a * b // i


num1 = int(input('请输入第一个正整数：'))

num2 = int(input('请输入第二个正整数：'))

list1 = list(range(min(num1, num2), 0, -1))

print(list1)

result = lcm(num1, num2)

print('{}和{}两个数的最小公倍数为{}'.format(num1, num2, result))
