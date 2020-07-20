# 捕获多个异常

try:
    num1 = input('请输入第一个数：')
    num2 = input('请输入第二个数：')
    result = int(num1) / int(num2)
    print(result)

    f = open('a.txt', 'r')
except ZeroDivisionError:
    print('除数不能为0！')

except FileNotFoundError:
    print('打开的文件不存在！')

except NameError:
    print('变量不存在！')