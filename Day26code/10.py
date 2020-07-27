# 多态： 在Python中，多态指在不考虑对象类型的情况下使用对象。


class Animal:
    """动物类"""
    def shout(self):
        print("动物正在叫……")


class Cat(Animal):
    """猫类"""
    def shout(self):
        print("喵喵喵……")


class Dog(Animal):
    """狗类"""
    def shout(self):
        print("汪汪汪……")


# 定义函数fn
def fn(temp):
    temp.shout()


dog = Dog()

fn(dog)

cat = Cat()

fn(cat)