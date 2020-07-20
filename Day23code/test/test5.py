# 让我们来做一个简单的 NLP（自然语言处理）任务。假设我们有一个文本文件 in.txt
#
# 下面是 NLP 任务的基本步骤：
# 1.读取文件；
import re

with open('../data/in.txt', 'r') as rf:
    text = rf.read()
    # print(text)

# 2.去除所有标点符号和换行符，并把所有大写变成小写；

text = re.sub(r'[^\w]', ' ', text)

text = text.lower()

print(text)
# 3.合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；

# 生成所有单词的列表

word_list = text.split(' ')

print(word_list)

# 去掉空白单词

word_list = filter(None, word_list)  # 返回的结果是迭代器函数，需要结合list函数转换程列表

# print(word_list)     # <filter object at 0x00000251E4ED6160>

word_list = list(word_list)

print(word_list)

word_dict = {}

for word in word_list:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

print(word_dict)

sorted_word_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

print(sorted_word_list)
# 4.将结果按行输出到文件 out.txt。

with open('../data/out.txt', 'w') as wf:
    for key, value in sorted_word_list:
        wf.write('{} {}\n'.format(key, value))