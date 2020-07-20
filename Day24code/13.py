# 异常使用的注意点

# 避免滥用异常处理

# 比如，查找字典中某个键对象的值

# try:
#     userinfo = {'name': 'caocao', 'age': 18, 'sex': '男'}
#     print(userinfo['city'])
# except Exception as err:
#     print('Exception:{}'.format(err))

# 建议以上这种情况，一般不要异常处理，直接通过流程控制进行处理
userinfo = {'name': 'caocao', 'age': 18, 'sex': '男'}

if 'city' in userinfo:
    print(userinfo['city'])