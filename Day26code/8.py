# 调用父类的方法

# 单继承


class Animal:
    """动物类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run(self):
        print("{}正在跑".format(self.name, self.age))


class Cat(Animal):
    """猫类"""

    def __init__(self, name, age):

        # 增加了自己的color属性
        self.color = "白色"

        # 调用父类的init方法
        super().__init__(name, age)


cat1 = Cat('Tom', 1)

print(cat1.name)

cat1.run()

print(cat1.color)