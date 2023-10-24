"""
    student_manager_system
        软件架构
            view -- controller -- model
"""


# 需求为向导
# 1、显示菜单
class StudentModel:
    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 由系统决定的全球唯一标识符
        self.sid = sid


class Studentview:
    """
        学生视图：负责输入输出相关功能
    """

    def __init__(self):
        self.controller = StudentController()

    def display_menu(self):
        print("1键录入学生信息")
        print("2键显示学生信息")
        print("3键删除学生信息")
        print("4键修改学生信息")

    def select_menu(self):
        item = input("请您输入选项:")
        if item == "1":
            self.input_student_info()
        elif item == "2":
            self.display_students()
        elif item == "3":
            self.delete_student()
        elif item == "4":
            self.change_student_info()

    def input_student_info(self):
        stu = StudentModel()
        stu.name = input("请输入人学生姓名:")
        stu.age = input("请输入人学生年龄:")
        stu.score = input("请输入人学生成绩:")
        self.controller.add_student(stu)
        # stu.sid由控制器赋值

    def display_students(self):
        for item in self.controller.list_student:
            print(f"姓名：{item.name}年龄：{item.age}成绩：{item.score}sid：{item.sid}")

    def delete_student(self):
        del_sid = int(input("请输入要删除学生的sid:"))
        if self.controller.delete_student(del_sid):
            print("删除成功！")
        else:
            print("删除失败！")

    def change_student_info(self):
        stu = StudentModel()
        stu.sid = int(input("请输入人学生sid:"))
        stu.name = input("请输入人学生姓名:")
        stu.age = int(input("请输入人学生年龄:"))
        stu.score = int(input("请输入人学生成绩:"))
        if self.controller.change_student_info(stu):
            print("修改成功！")
        else:
            print("修改失败！")


class StudentController:
    def __init__(self):
        self.list_student = []
        self.start_sid = 1001

    def add_student(self, new_stu):
        # 自增长
        new_stu.sid = self.start_sid
        self.start_sid += 1
        self.list_student.append(new_stu)

    def delete_student(self, del_sid):
        for i in range(len(self.list_student)):
            if del_sid == self.list_student[i].sid:
                del self.list_student[i]
                return True
        return False

    def change_student_info(self, stu):
        for item in self.list_student:
            if stu.sid == item.sid:
                # item.name = stu.name
                # item.age = stu.age
                # item.score = stu.score
                item.__dict__ = stu.__dict__
                return True
        return False


# ---------------------------------入口-------------------------------
view = Studentview()
while True:
    view.display_menu()
    view.select_menu()
