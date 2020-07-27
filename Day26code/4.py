# 封装

# 通常把隐藏属性、方法和方法实现细节的过程称为封装。
# 封装的作用：为了保护类里面的属性，避免外界随意赋值。


class Person:

    def __init__(self, name, age, sex):
        """构造方法"""
        self.name = name
        self.__age = age  # 私有属性
        self.sex = sex

    def say(self):
        return "我叫{}，我是{}的，今年{}岁了。".format(self.name, self.sex, self.__age)

    def get_age(self):
        """获取私有属性_age的值"""
        return self.__age

    def set_age(self, new_age):
        """
        设置私有属性_age的值
        :param new_age: 新的年龄值
        """
        # 判断传入的参数是否符合要求，符合要求才能赋值
        if new_age > 0 and new_age <= 120:
            self.__age = new_age


p1 = Person('张三', 28, '男')

print(p1.say())

print(p1.get_age())

p1.set_age(300)

print(p1.get_age())

p1.set_age(120)

print(p1.get_age())
# print(p1.age)

# p1.age = 29
#
# print(p1.age)

