# raise 语句案例
# 例如：用户登录过程中发生了输入账号或密码错误时，可以使用raise实现主动抛出异常，由异常处理语句进行错误处理。

try:
    account = input('请输入登录账号：')
    if account != "hqhiwqy":
        raise Exception('账号错误，请重新输入！')

    password = input('请输入登录密码：')
    if password != "123456":
        raise Exception('密码错误，请重新输入！')

except Exception as err:
    print('提示：{}'.format(err))
else:
    print('登录成功')