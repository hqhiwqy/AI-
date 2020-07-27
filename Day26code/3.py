# 运算符重载 通过实现特定的方法，使类的实例对象也能够支持Python的各种内置的操作。

# 索引和分片重载

# __getitem__
# __setitem__
# __delitem__

class Demo:

    def __init__(self, data):
        """
        构造方法
        :param data:
        """
        self.data = data

    def __getitem__(self, index):
        """
        获取索引、分片运算符重载方法
        :param index:索引
        :return:self.data[index]
        """
        return self.data[index]


demo = Demo([1, 2, 3, 4])

print(demo[1])
print(demo[:])

# 定制对象的字符串形式

# __repr__
# __str__

# 只重载 __str__ 方法


class Demo2:
    one = 100

    def __str__(self):
        # 返回自定义的字符串
        return "one=%s" %self.one

demo2 = Demo2()

print(str(demo2))
print(repr(demo2))  # 调用repr函数，结果显示没有进行替换


# 只重载 __repr__ 方法


class Demo3:
    one = 100

    def __repr__(self):
        # 返回自定义的字符串
        return "one=%s" %self.one


demo3 = Demo3()

print(str(demo3))
print(repr(demo3))

# 同时重载__str__方法和__repr__

class Demo4:

    one = 100

    def __str__(self):
        # 返回自定义的字符串
        return "STR转换: one=%s" % self.one
    def __repr__(self):
        # 返回自定义的字符串
        return "REPR转换: one=%s" % self.one


demo4 = Demo4()
print(demo4)
print(str(demo4))
print(repr(demo4))
