# finally 终止行为

try:
    f = open('a.txt', 'w')
    content = f.read()
    print(content)
except Exception as err:
    print(err)

finally:
    print('无论是否有异常产生，都会执行这里的代码块！')
    f.close()