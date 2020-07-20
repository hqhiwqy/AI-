# 文件夹的相关操作

import os

# os.mkdir('a')     # 创建文件夹

current_dirname = os.getcwd()

print(current_dirname)  # 查看当前目录

# os.chdir("../")  # 更改目录
#
# current_dirname = os.getcwd()
#
# print(current_dirname)

dir_list = os.listdir("./")  # 查看目录

print(dir_list)

# os.rmdir('./data/son')  # 删除目录
# rmdir只能删除空的文件夹