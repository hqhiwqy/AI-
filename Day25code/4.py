import re

# 案例三：替换字符串中的不良内容


def main():
    text = 'cnm nmsl 傻逼 脑残 你好啊 早上好'
    result = re.sub(r'cnm|nmsl|傻|脑|草', '*', text, flags=re.IGNORECASE)
    print(result)


if __name__ == '__main__':
    main()