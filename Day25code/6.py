import re

# 案例五：匹配中文


def main():
    text = '你好！ hello china ! 中国！  您好！'

    # 创建一个正则表达式对象，用来匹配中文

    # 中文对应Unicode编码范围在[u4e00-u9fa5]
    pattern = re.compile(r'[\u4e00-\u9fa5]+')

    result = re.findall(pattern, text)

    print(result)


if __name__ == '__main__':
    main()