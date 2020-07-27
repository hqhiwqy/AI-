import re

# 案例一：验证输入用户名和QQ号是否有效对应的提示信息

# 要求：用户名必须由字母、数字、下划线构成，且长度要在6-20个字符之间


def main():

    username = input('请输入用户名：')
    qq = input('请输入QQ号：')

    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('用户名必须由字母、数字或下划线构成且长度要在6-20个字符')

    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('QQ号必须5-12的数字且首位不为0')


if __name__ == '__main__':
    main()
