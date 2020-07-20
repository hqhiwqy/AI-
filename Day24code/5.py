# 没有捕获搭配异常

try:
    name = 'caocao'
    print(name)
except Exception as err:
    print(err)
else:
    print('没有捕获到异常！')