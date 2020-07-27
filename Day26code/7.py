# 多继承


class Bird:
    """鸟类"""
    def fly(self):
        print("鸟儿正在天空中飞……")


class Fish:
    """鱼类"""
    def swim(self):
        print("鱼儿正在水里游……")


class WaterBird(Bird, Fish):
    """水鸟类"""
    pass


wb1 = WaterBird()

wb1.fly()

wb1.swim()