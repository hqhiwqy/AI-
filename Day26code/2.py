# 面向对象过程就是分析出解决问题的步骤，
#   然后用函数把这些步骤一一实现，
#   使用的时候一个一个一次调用即可。

# 面向对象则是把解决问题的事务分解成多个对象，
#   而建立对象的目的也不是为了完成一个个步骤，
#   而是为了描述某个事务在解决整个问题的过程中所发生的行为。


# 类的定义及调用

class Person:

    # 构造方法
    def __init__(self, name, age, sex):
        """
        构造方法
        :param name: 姓名
        :param age:  年龄
        :param sex:  性别
        """
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        """析构方法"""
        print("---------析构方法---------")

    def say(self):
        """说话"""
        print("我叫{}，今年{}岁。".format(self.name, self.age))


p1 = Person('张三', 28, '男')

del p1

print('---------------')

# p1.say()

# Python有自动回收垃圾的机制，当Python程序借宿的时候，Python解释器回检测当前是否需要释放内存空间
# 如果有需要释放的内存空间，就会自动调用析构方法进行释放。如果程序中已经手动添加了 del 语句，就不再自动删除。
