"""
    有一家公司有如下几种岗位：
        --程序员：底薪 + 项目分红
        --测试员：底薪 + bug数*5
        --...
    创建员工管理器：
        --记录所有员工
        --计算所有员工的总薪资
"""


class WorkerManagement:
    def __init__(self):
        self.__list_workers = []

    def add_workers(self,workers):
        if isinstance(workers,Worker):
            self.__list_workers.append(workers)

    def get_total_salary(self):
        total_salary = 0
        for item in self.__list_workers:
            total_salary += item.calculate_salary()
        return total_salary


class Worker:
    def __init__(self, base_salary=0):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class programmer(Worker):
    def __init__(self, base_salary=0, program_salary=0):
        # self.base_salary = base_salary
        super().__init__(base_salary)
        self.program_salary = program_salary

    def calculate_salary(self):
        return super().calculate_salary() + self.program_salary


class tester(Worker):
    def __init__(self, base_salary=0, bug_num=0):
        # self.base_salary = base_salary
        super().__init__(base_salary)
        self.bug_num = bug_num

    def calculate_salary(self):
        return super().calculate_salary()  + self.bug_num * 5


# -----------------------------------------------------------------------------------
test01 = WorkerManagement()
test01.add_workers(programmer(1000,100))
test01.add_workers(tester(800,200))
num = test01.get_total_salary()
print(num)
