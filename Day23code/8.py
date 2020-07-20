# ======================
# 学生管理系统（V1.0.0）
# 1.添加学生的信息
# 2.修改学生的信息
# 3.删除学生的信息
# 4.显示学生的信息
# 0.退出系统
# =======================

# 定义一个用来保存学生信息的列表

student_infos = []


def print_menu():
    """
    打印功能菜单
    """
    print('=' * 30)
    print('学生管理系统——V1.0.0')
    print('1.添加学生的信息')
    print('2.修改学生的信息')
    print('3.删除学生的信息')
    print('4.显示学生的信息')
    print('0.退出系统')
    print('=' * 30)


def add_info():
    """
    用于添加学生信息的函数
    """
    name = input('请输入学生姓名：')
    sex = input('请输入学生的性别（男/女）：')
    phone = input('请输入学生的手机号码：')

    info_dict = {}
    info_dict['name'] = name
    info_dict['sex'] = sex
    info_dict['phone'] = phone
    student_infos.append(info_dict)


def delete_info():
    """
    用于删除学生信息的函数
    """
    delete_index = int(input('请输入要删除的序号：')) - 1
    del student_infos[delete_index]


def modify_info():
    """
    用于修改学生信息的函数
    """
    modify_index = int(input('请输入要修改的序号：')) - 1
    name = input('请输入新学生的姓名：')
    sex = input('请输入新学生的性别（男/女）：')
    phone = input('请输入新学生的手机号码：')
    student_infos[modify_index]['name'] = name
    student_infos[modify_index]['sex'] = sex
    student_infos[modify_index]['phone'] = phone


def display_info():
    """
    显示所有学生信息的函数
    """
    print('所有学生信息如下：')
    print('编号     姓名     性别    手机号')
    i = 0
    for item in student_infos:
        print("{}        {}     {}     {}".format(i, item['name'], item['sex'], item['phone']))
        i += 1


def main():
    """
    主函数控制整个程序的流程和逻辑
    """
    while True:
        print_menu()
        key = int(input('请输入功能菜单对应的数字指令：'))
        if key == 1:
            add_info()
        elif key == 2:
            modify_info()
        elif key == 3:
            delete_info()
        elif key == 4:
            display_info()
        elif key == 0:
            quit_confirm = input('你确定退出系统吗？（Y/N）:')
            if quit_confirm == 'Y' or quit_confirm == 'y':
                break
            else:
                print('输入有误，请重新输入！')


main()
