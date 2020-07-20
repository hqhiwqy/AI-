# 自定义异常

class ShortInputException(Exception):
    """
    自定义异常类
    """

    def __init__(self, length, atleast):
        self.length = length  # 输入的长度
        self.atleast = atleast  # 至少的长度

try:
    pwd = input('请输入你的密码：')
    if len(pwd) < 6:
        raise ShortInputException(len(pwd), 6)

except ShortInputException as result:
    print('ShortInputException：输入的长度是{}，长度至少应该为{}'.format(result.length, result.atleast))
else:
    print('没有发生异常')