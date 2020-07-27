from math import sqrt
# 静态方法

# 例如我们定义一个三角形类，通过传入三条边长来构造三角形，并提供计算周长和面积的方法
# 另外还需要一个方法来检测三条边长是否构成一个三角形。显然，这个检测的方法不是我们三角形类的实例对象。


class Triangle:
    """三角形类"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """
        检测三条边长是否构成一个三角形
        :param a: 边长a
        :param b: 边长b
        :param c: 边长c
        :return:  True | False
        """
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """周长"""
        return self.a + self.b + self.c

    def area(self):
        """面积"""
        half = self.perimeter() / 2

        return sqrt(half * (half-self.a) * (half-self.b) * (half-self.c))


if __name__ == "__main__":
    a, b, c = 1, 2, 3
    if Triangle.is_valid(a, b, c):
        t1 = Triangle(a, b, c)
        print(t1.area())
    else:
        print('无法构成三角形！')
