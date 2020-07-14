# 5、编写函数，判断一个整数是否是回文数。（回文数是一个正向和逆向都相同的整数，如123321、9889）


def huiwenshu(n):
    if n == n[::-1]:  # 正向和逆向是否相同
        print("%s是回文数" % n)
    else:
        print("%s不是回文数" % n)


n = input('请输入一个数字：')

huiwenshu(n)