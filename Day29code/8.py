import re

content = "111111\n222222\n333333\n444444"

# 多行匹配

res1 = re.findall(r'.+', content)

res2 = re.findall(r'.+', content, re.M)

# 单行匹配

res3 = re.findall(r'.+', content, re.S)

print(res1)
print(res2)
print(res3)

# zip函数

list1 = [1, 2, 3]
list2 = [5, 6, 7]

for x, y in zip(list1, list2):
    print(x, y, x*y)
