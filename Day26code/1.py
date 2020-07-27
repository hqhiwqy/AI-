import re
# Python中正则表达式 .*和.*？的区别？

# . 匹配任意除了换行符（\n）以外的字符
# * 表示匹配0次或无限次
# .* 表示贪婪模式
# +或*后面跟上？表示非贪婪模式

text = "aabab"

pattern = re.compile(r'a.*b')  # 贪婪模式

result = re.findall(pattern, text)

pattern = re.compile(r'a.*?b')  # 非贪婪模式

result2 = re.findall(pattern, text)

print(result, result2)


# 思考题：from module_name import * 和 import module_name 有什么区别呢？

# import module_name 更安全 更好用


# Python中用正则表达式提取字符串中所有的域名（URL）

pattern3 = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

url = 'http://www.baidu.com'

result3 = re.findall(pattern3, url)

print(result3)

# 编写一个函数，实现读入一个字符串str，输出字符串str中的连续最长的数字串。


def max_count_str(str):
    """
    返回参数str中的连续最长的数字串
    :param str: 带有数字的str
    :return:
    """
    pattern = re.compile(r'\d+')
    num_list = re.findall(pattern, str)

    print(num_list)

    result = sorted(num_list,key=lambda x: len(x), reverse=True)

    return result[0]
    # temp = 1
    # for i in range(len(num_list)):
    #     print(i)
    #     if len(num_list[i]) > temp:
    #         temp = len(num_list[i])
    #         index = i
    # return num_list[index]


text = "l1acf222ddfdf123456734423wegghjhjj8776823ddfg"

print(max_count_str(text))

