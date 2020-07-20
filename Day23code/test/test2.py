# 2.定义一个函数，实现删除指定文件夹的功能（需要考虑非空文件夹的情况）
import os


def del_dir(path):
    """
    删除指定文件夹
    :param path:需要删除的文件夹路径
    :return:
    """
    if not os.path.exists(path):
        print("{} not exist.".format(path))
        return

    if not os.path.isdir(path):
        print("{} not a dicectory".format(path))
        return

    list_dir = os.listdir(path)
    # print(list_dir)

    for file_name in list_dir:
        # 拼接文件的完整路径
        # file_path = path + "/" + file_name
        file_path = os.path.join(path, file_name)
        # 判断每一个文件是一个普通文件还是文件夹
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("File：{} was removed.".format(file_path))
        elif os.path.isdir(file_path):
            # 自己调用自己
            del_dir(file_path)
            print("Directory: {} was removed.".format(file_path))
    os.rmdir(path)

    print("{} has been deleted!".format(path))


del_dir("../data")