# 1.读取一个文件，显示出了 # 开头的行的所有行

f = open('../data/a.txt', 'r')

lines = f.readlines()

f.close()

print(lines)

new_lines = list(filter(lambda x: x[0] == "#", lines))

print(new_lines)

f = open('../data/a.txt', 'w')

f.writelines(new_lines)  # 保留了 # 行

f.close()

# 对于"r+"来说，先读取了内容，再写入的话就变成了追加模式：如果直接写入内容，就是部分覆盖。

f = open('../data/a.txt', 'r+')

lines = f.readlines()

print(lines)

new_lines = list(filter(lambda x: x[0] == "#", lines))

f.writelines(['#aaaaaaaaaaaaaaa\n', 'bbbbbbbbbbbbbbbb\n'])

f.close()