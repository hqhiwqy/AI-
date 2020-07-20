# with 上席文表达式 as 资源对象：
#    对象的操作

try:
    with open("a.txt") as rf:
        content = rf.read()
        print(content)
except Exception as err:
        print(err)