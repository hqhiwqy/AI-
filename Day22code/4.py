# 名片管理器

info_list = []


# 输出名片管理器菜单


def display_menu():
    print("=" * 30)
    print("名片管理器 V2.0.0")
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
    phone = input('请输入你的手机号：')
    work = input('请输入你的工作：')
    info_list.append([name, phone, work])


# 修改名片


def edit_info():
    edit_index = int(input('请输入要修改的序号：')) - 1
    print('*' * 20)
    print("1.修改姓名")
    print("2.修改手机号")
    print("3.修改工作")
    print("4.全部修改")
    edit_new_info = int(input('请输入功能对应得数字：'))
    if edit_new_info == 1:
        new_name = input('请输入新的名字:')
        info_list[edit_index] = new_name
    elif edit_new_info == 2:
        pass
    elif edit_new_info == 3:
        pass
    elif edit_new_info == 4:
        new_info = input('请输入新的信息：')
        info_list[edit_index] = new_info


# 删除名片


def delete_info():
    delete_index = int(input('请输入要删除的序号：')) - 1
    del info_list[delete_index]


# 查看所有名片


def show_info():
    for i in info_list:
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
