# 可变参

# args——用来将参数打包成元组给函数体调用
# **kwargs——用来将参数打包程字典给函数体调用
# 注意：参数arg、*args、**kwargs 参数的位置必须是(arg、*args、**kwargs)这个顺序，否则程序回报错


def demo(arg, *args, **kwargs):
    print("arg: {}".format(arg))
    print("*args: {}".format(args))
    print("**kwargs: {}".format(kwargs))


demo(1, 2, 3, 4, 5, 6, a=1, b='2', c=3)

demo(1, a=1, b=2, c=3)