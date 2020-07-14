# 随机数函数
# random.random     返回0与1之间的随机浮点数N，范围为 0 <= N < 1
# random.randint(a, b)    返回一个随机的整数N，范围为 a <= N <= b，a < b
# random.choice(seq)  从序列 seq 中返回一个随机的元素
# random.shuffle(x)  将列表中的元素打乱顺序
# random.sample(seq.x)  从指定序列中随机获取x个元素组成一个新的子序列进行返回，不会修改原有序列


import random
print(random.random())

print(random.randint(0, 2))

print(random.choice('python'))

print(random.choice(['html', 'css', 'python', 'js', 'go']))

list1 = ['html', 'css', 'python', 'js', 'go']

random.shuffle(list1)

print(list1)

slice = random.sample(list1, 2)

print(slice)