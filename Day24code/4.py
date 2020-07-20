# 捕获所有的异常

try:
    num1 = input('请输入第一个数：')
    num2 = input('请输入第二个数：')
    result = int(num1) / int(num2)
    print(result)

    f = open('a.txt', 'r')
except Exception as err:
    print(err)
