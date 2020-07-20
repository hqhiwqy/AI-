# 捕获简单异常
try:
    num1 = input('请输入第一个数：')
    num2 = input('请输入第二个数：')
    result = int(num1) / int(num2)
    print(result)

except ZeroDivisionError:
    print('除数不能为0！')