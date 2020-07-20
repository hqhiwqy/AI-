# raise 语句

# 使用类名引发异常

# raise IndexError

# 使用异常类的实例引发的异常

name_error = NameError
# raise name_error

# 传递异常

# try:
#     raise NameError
# except:
#     print('出错了')
#     raise  # 再次引发刚刚发生过的异常

# 指定异常的描述信息
# raise IndexError('索引下标超出范围')

# 异常引发异常（raise from）
try:
    print(age)
except Exception as err:
    raise IndexError('索引下标超出范围') from err