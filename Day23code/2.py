# 装饰器

# 定义一个登录校验的装饰器函数


def login_require(fn):
    print('我是外函数1')
    """
    登录校验的装饰器函数
    :param fn: 被装饰的函数
    :return inner: 返回内函数
    """

    def inner(*args, **kwargs):
        print('这是内函数')
        print(args)
        print(kwargs)
        return fn(*args, **kwargs)

    return inner


@login_require
def add(*args, **kwargs):
    return "Add"


def delete():
    return "Delete"


print(add(1, 2, 3))
