# 异常完整语句

try:
    # 语句块
    f = open('a.txt', 'w')
    content = f.read()
    print(content)
except Exception as err:
    # 异常处理代码
    print(err)
else:
    # 没有捕获到异常
    pass
finally:
    # 无论是否有异常产生，都会执行这里的代码块
    print('无论是否有异常产生，都会执行这里的代码块！')
    f.close()