# 闭包

# 编写一个函数，计算一个整数的n次幂


# 不使用闭包
def nth_power_other(base, exponent):
    return base ** exponent


print(nth_power_other(2, 2))
print(nth_power_other(2, 3))


# 使用闭包
def nth_power(exponent):

    def exponent_of(base):

        return base ** exponent

    return exponent_of  # 返回内部函数exponent_of


# 计算一个数的平方


square = nth_power(2)

# 计算一个数的立方

cube = nth_power(3)

# print(square, cube)

print(square(2))  # 2的平方

print(cube(4))  # 4的立方