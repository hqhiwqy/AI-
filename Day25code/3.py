import re
# 案例二：从一段文字中提取出国内手机号码


def main():
    text = "手机号记住是16603584018 还有13834766974，不是119，不是110"

    # 创建一个正则表达式对象

    pattern = re.compile(r'(?<=\D)1[345678]\d{9}(?=\D)')

    phone_list = re.findall(pattern, text)

    print(phone_list)

if __name__ == '__main__':
    main()