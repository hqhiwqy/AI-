# 多个装饰器

# 多个装饰器可以应用在同一个函数上，它们的调用是自下而上的。


def login_require(fn):
    print('我是装饰器函数1')
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


def auth_require(fn):
    print('我是装饰器函数2')

    def inner(*args, **kwargs):
        print('这是内函数')
        print(args)
        print(kwargs)
        return fn(*args, **kwargs)

    return inner


@auth_require
@login_require
def add(*args, **kwargs):
    return "Add"


def delete():
    return "Delete"


print(add(1, 2, 3))
