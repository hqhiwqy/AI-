# 重写父类的方法


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("我叫{}，今年{}岁了".format(self.name, self.age))


class Chinese(Person):
        def say(self):
            print("你好")


chinese = Chinese('张三', 18)

chinese.say()

p1 = Person('草草', 20)

p1.say()