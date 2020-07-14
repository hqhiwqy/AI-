# 名片管理器

name_list = []


# 输出名片管理器菜单


def display_menu():
    print("=" * 30)
    print("名片管理器 V1.0.0")
    print("1.添加名片")
    print("2.修改名片")
    print("3.删除名片")
    print("4.查看所有名片")
    print("5.退出系统")
    print("=" * 30)


# 获取用户输入的信息
def get_choice():
    key = input('请输入功能对应得数字：')
    return int(key)


# 添加名片

def add_info():
    name = input('请输入姓名：')
    name_list.append(name)


# 修改名片


def edit_info():
    edit_index = int(input('请输入要修改的序号：')) - 1
    new_name = input('请输入新的姓名：')
    name_list[edit_index] = new_name


# 删除名片


def delete_info():
    delete_index = int(input('请输入要删除的序号：')) - 1
    del name_list[delete_index]


# 查看所有名片


def show_info():
    for i in name_list:
        print(i)


# 退出系统

def quit():
    pass


# 定义一个main函数，用于控制整个程序的流程


def main():
    while True:
        display_menu()  # 打印菜单
        key = get_choice()
        if key == 1:
            add_info()
        elif key == 2:
            edit_info()
        elif key == 3:
            delete_info()
        elif key == 4:
            show_info()
        elif key == 5:
            quit_confirm = input('真的要退出嘛？(y/n)')
            if quit_confirm == 'y' or 'Y':
                break
            else:
                print('你输入有误，请重新输入！')


main()
