# 函数的嵌套调用


def func_one():
    print('我是func_one函数执行的代码')


def func_two():
    print('-----func_two start-----')
    func_one()
    print('-----func_two end-----')


func_two()


def f1():
    print('hello')

    def f2():
        print('world')

    f2()


f1()
# f2()  # 内部函数只能被外部函数所调用和访问，不会暴露在全局作用域。

# 举例

# def connect_DB():

   # def get_DB_config():
        # ...
        # return host, username, password

  #  conn = connector.connect()
  #  return conn


# 递归函数
# 递归函数是指在一个函数中调用了函数本身。
# 案例：计算阶乘 n! = 1*2*3*4*5*…*n

def func(count):
    if count == 1:
        result = 1
    else:
        result = func(count - 1) * count
    return result


print(func(3))
print(func(5))

# 函数嵌套调用的作用：合理的使用函数嵌套，能够提高程序的运行效率

# 编写一个函数，计算一个整数的n次幂


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