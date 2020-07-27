import re

# 案例四：拆分长字符串


def main():
    text = "窗前明月光，疑是地上霜。举头望明月，低头思故乡。"

    result = re.split(r'[，。，。]', text)

    print(result)

    while '' in result:
        result.remove('')

    print(result)


if __name__ == '__main__':
    main()