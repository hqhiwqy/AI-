# 引入单个模块
# import module_name1

# import time, os

# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# 引入多个模块
# import module_name1, module_name2 ……
# os.mkdir('./test')


# 引入模块中的函数

# from module_name1 import fn1, fn2, ……
# from module_name import *

from time import *

print(strftime("%Y-%m-%d %H:%M:%S", localtime()))

# 注意：   1.import同一个模块只会执行一次
#         2.除了一些特殊情况，import必须位于程序的最前端
#         3.在py3中，_init_.py 不是必须要有的