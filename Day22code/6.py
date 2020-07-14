# 函数的变量作用域

x = 200  # 全局变量


def f1():
    x = 100
    print(x)  # 局部变量


f1()
print(x)

y = 100


def f2():
    global y  # global——在函数作用域中修改全局变量
    y += 100
    print(y)


f2()


def f3():
    a = 1

    def f4():
        nonlocal a  # nonlocal——用于在函数作用域中修改嵌套作用域的变量
        a = 2

    f4()
    print(a)


f3()
