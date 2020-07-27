# 某公司有三种类型的员工，分别是部门经理、程序员、销售员。现在需要你设计一个工资结算系统，可根据提供的员工信息来计算月薪：
# 部门经理的月薪是每月固定15000元；
# 程序员的月薪是按本月工作时间计算，每小时150元；
# 销售员的月薪是1200元底薪+销售额5%的提成。
# 提示：isinstance() 函数——判断对象是否是一个已知的类型。

# 使用模块abc中的ABC类来派生抽象基类
from abc import ABC, abstractmethod


class Employee(ABC):
    """员工"""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # 使用修饰器 @abstractmethod 来表示抽象方法
    @abstractmethod
    def get_salary(self):
        """获取月薪"""
        pass


class Manager(Employee):
    """部门经理类"""
    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员类"""
    def __init__(self, name, work_hour=0):
        super().__init__(name)
        self._work_hour = work_hour

    @property
    def work_hour(self):
        return self._work_hour

    @work_hour.setter
    def work_hour(self, value):
        self._work_hour = value

    def get_salary(self):
        return self._work_hour * 150.0


class Saleman(Employee):
    """销售员"""
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        self._sales = value

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


if __name__ == "__main__":
    employee_list = [Manager('张三'), Programmer('李四'), Saleman('王五')]

    for item in employee_list:
        if isinstance(item, Programmer):
            item.work_hour = int(input('请输入{}本月的工作时间：'.format(item.name)))
        elif isinstance(item, Saleman):
            item.sales = float(input('ing输入{}本月的销售额：'.format(item.name)))

        print('{}本月工资为{}'.format(item.name, item.get_salary()))