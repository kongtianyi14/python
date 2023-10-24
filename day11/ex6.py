"""
# 员工信息管理系统(员工编号/部门编号/姓名/工资)
"""


class WorkerModel:
    def __init__(self, wid = 0, apartment = "", name = "", salary=0):
        self.wid = wid
        self.apartment = apartment
        self.name = name
        self.salary = salary


class WorkView:
    def __init__(self):
        self.controller = Controller()

    def main_mune(self):
        print("1键录入工人信息")
        print("2键显示工人信息")
        print("3键删除工人信息")
        print("4键修改工人信息")

    def select_mune(self):
        item = input("请您输入选项:")
        if item == "1":
            self.input_workers_info()
        elif item == "2":
            self.display_workers()
        elif item == "3":
            self.delete_worker()
        elif item == "4":
            self.change_worker_info()
    # 录入信息
    def input_workers_info(self):
        worker = WorkerModel()
        worker.name = input("请输入工人的姓名:")
        worker.apartment = input("请输入工人的部门:")
        worker.salary = int(input("请输入工人的工资:"))
        self.controller.input_workers_info(worker)
    #查看
    def display_workers(self):
        self.controller.display_workers()

    #删除
    def delete_worker(self):
        del_wid = int(input("请输入要删除工人的wid:"))
        if self.controller.delete_worker(del_wid):
            print("删除成功")
        else:
            print("删除失败")

    #修改
    def change_worker_info(self):
        change_worker = WorkerModel()
        change_worker.name = input("请输入工人的姓名:")
        change_worker.apartment = input("请输入工人的部门:")
        change_worker.salary = int(input("请输入工人的工资:"))
        change_worker.wid = int(input("请输入工人的wid:"))
        if self.controller.change_worker_info(change_worker):
            print("修改成功")
        else:
            print("修改失败")


# worker.wid = int(input("请输入工人的姓名"))
# wid由Controller决定

class Controller:
    def __init__(self):
        self.list_workers = []
        self.start_wid = 1001

    def input_workers_info(self, worker):
        worker.wid = self.start_wid
        self.start_wid += 1
        self.list_workers.append(worker)

    def display_workers(self):
        for item in self.list_workers:
            print(f"姓名：{item.name},工资：{item.salary},部门：{item.apartment},wid：{item.wid}")

    def delete_worker(self, del_wid):
        for i in range(len(self.list_workers)):
            if self.list_workers[i].wid == del_wid:
                del self.list_workers[i]
                return True
        return False

    def change_worker_info(self, change_worker):
        for item in self.list_workers:
            if item.wid == change_worker.wid:
                item.__dict__ = change_worker.__dict__
                return True
        return False


A = WorkView()
while True:
    A.main_mune()
    A.select_mune()

