import re
# 数量词的贪婪模式和非贪婪模式

text = "abbbc"

# Python中默认是贪婪模式

result = re.findall(r'ab*', text)

print(result)   # ['abbb']

# 非贪婪模式

result = re.findall(r'ab*?', text)

print(result)  # ['a']

