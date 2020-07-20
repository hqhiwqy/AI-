# assert 语句

try:
    num = 0
    assert num != 0, "num,的值不能为0！"
except Exception as err:
    print(err)