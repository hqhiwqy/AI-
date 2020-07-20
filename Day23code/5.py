# 打开文件

f = open('./data/a.txt', 'r')

# 读取文件中的全部数据

content = f.read()
print(content)

f = open('./data/b.txt', 'r')

# 从文件中一行一行的读取数据
line1 = f.readline()

line2 = f.readline()

print(line1, line2)

f.close()

f = open('./data/c.txt', 'w')

f.write("aaaaaaaa\nbbbbbbbb\ncccccccc\n")

f.close()

f = open('./data/c.txt', 'a')

f.write("aaaaaaaa\nbbbbbbbb\ncccccccc\n")

f.close()


