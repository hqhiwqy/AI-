# 7、编写函数，判断输入的三个数字是否能构成三角形的三条边。

from math import sqrt


def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print('不能构成三角形，三角形的三条边都必须大于0')
    elif a + b <= c or b + c <= a or c + a <= b:
        print('不能构成三角形，三角形两边之和必须大于第三边')
    else:
        print('输入的三个数字可以构成三角形的三条边')


a = float(input('请输入边长a：'))
b = float(input('请输入边长b：'))
c = float(input('请输入边长c：'))
triangle(a, b, c)


# 解法2

# 两边之和大于第三边，两边之差小于第三边

num_list = sorted(map(int, input('请分别输入三条边长(按空格隔开)：').split()))
print(num_list)

if sum(num_list[:2]) <= num_list[2] or num_list[2] - num_list[0] >= num_list[1]:
    print('无法构成三角形')
else:
    print('可以构建三角形')

    # 求面积

    # 利用海伦公式
    p = 0.5 * sum(num_list)  # 半周长
    s = sqrt(p * (p - num_list[0]) * (p - num_list[1]) * (p - num_list[2]))
    print("三角形的面积为{}".format(s))

# map(function, seq)——根据提供的函数对指定的序列做映射

# res = sorted(map(int, list1))

# print(res)