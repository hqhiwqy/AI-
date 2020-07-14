# 日期时间函数

# 时间戳

import time

ticks = time.time()

print('当前的时间戳为：{}'.format(ticks))

print(time.localtime())  # 查看localtime

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))  # 打印当前时间

# 日历函数

import calendar

print(calendar.month(2020, 7))
