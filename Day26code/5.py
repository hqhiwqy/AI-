# 实际开发中，建议是将属性命名以单下划线开头，通过这种方式暗示属性受保护，不建议外界直接访问
# 可以考虑使用 @property装饰器getter和setter方法


class Person:

    def __init__(self, name, age):
        """构造方法"""
        self._name = name
        self._age = age

    # 访问器——getter
    @property
    def name(self):
        return self._name

    # 修改器——setter
    @name.setter
    def name(self, value):
        self._name = value

    # 访问器——getter
    @property
    def age(self):
        return self._age

    # 修改器——setter
    @age.setter
    def age(self, value):
        if value < 0 and value > 120:
            return "年龄必须在0-120之间"
        self._age = value

    def play(self):
        if self._age < 16:
            return "{}正在玩吃鸡游戏".format(self._name)
        else:
            return "{}正在玩成人游戏".format(self._name)


p1 = Person('张三', 14)

print(p1.play())

# print(p1._age)  # 不要直接访问

p1.age = 22

print(p1.play())