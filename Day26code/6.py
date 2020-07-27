# 继承
# 单继承


class Animal:
    """动物类"""

    def __init__(self, name, color):
        self.name = name
        self.__color = color

    def run(self):
        print("{}的{} 正在跑".format(self.__color, self.name))


class Cat(Animal):
    """猫类"""
    def test(self):
        print(self.__color)  # 注意：父类的私有属性和私有方法是不能被子类所继承的。


cat1 = Cat('Tom', '白色')

cat1.run()

cat1.test()  # AttributeError: 'Cat' object has no attribute '_Cat__color'