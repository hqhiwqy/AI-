print("Hello World!")
print("Hello World!")
print("Hello World!")

# 定义一个变量name，并赋值

name = 'caocao'
print(name)  # 打印输出变量name

# 行与缩进

# Python最具特色的就是使用缩进来表示代码块

# 情况1：不在同一个代码块，所以不会报错
if True:
    print('True')
else:
    print('False')
print('-------------')

# 情况2：同一个代码块，缩进不一致，编译会出现错误
if True:
    print('True')
else:
    print('False')
  # print('-------------')

# 语句换行

# Python建议每行代码长度不超过80字符，对于过长的代码可以在语句的外侧添加一对圆括号，将其进行换行显示

newsStr1 = ("写 Python 代码时，你会严格遵守 pep8 规范么？"
           "还是要遵守的，不然代码传到 github 或者知乎上被人怼就不好了。"
           "但是如果靠肉眼去检查和注意的话，" 
           "太累，靠 PyCharm 来做这事就好，Command+Option+L，一键 pep8 走起。")

newsStr2 = "如果你是新手，可能会为了安装库而感到烦恼，" \
           "在 PyCharm 里面可以使用你熟悉的图形化界面来安装库，就不用陷在一堆命令行里了。"

