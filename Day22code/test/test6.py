# 6、双色球选号
#
# 题目：请通过Python实现双色球随机选号的功能，要求每次都会生成一个双色球随机选号的结果。
#
# 描述：双色球是中国福利彩票的一种玩法。它分为红色球号码区和蓝色球号码区，每注投注号码是由6个红色球号码和1个蓝色球号码组成，红色球号码从1-33中选取，蓝色球号码从1-16中选取。
import random


def random_balls():
    """
    随机产生一组双色球号码(6红球+1蓝球)
    :return:
    """

    # 红色6个，从1-33中选取

    red_balls = [x for x in range(1, 34)]

    # print(red_balls)

    balls = random.sample(red_balls, 6)
    balls.sort()  # 从小到大排列
    # print(balls)

    # 蓝色球1个 从1-16中选取
    blue_ball = random.randint(1, 16)
    balls.append(blue_ball)
    # print(balls)

    return balls


def display_balls(balls):
    """
    打印输出列表中的双色球号码
    :param balls:  存储双色球号码列表
    :return:
    """
    for ball in balls:
        print("%02d" % ball, end=' ')  # "%02d" % 前置补零
    print()


num = int(input('请输入机选的注数：'))

for _ in range(num):
    display_balls(random_balls())
random_balls()
