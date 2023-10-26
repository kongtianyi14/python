"""
    继承
class 父类:
    def 父类方法(self):
        方法体
class 子类(父类)：
    def 子类方法(self):
        方法体
儿子 = 子类()
儿子.子类方法()
儿子.父类方法()

(1) isinstance(对象, 类型)
返回指定对象是否是某个类的对象。
(2) issubclass(类型，类型)
返回指定类型是否属于某个类型。
"""
#适用性：多个类型，代码上有共性且概念上统一
#父类体现共性，子类体现个性
class Person:
    def say(self):
        print("说话")
class Teacher(Person):
    def teach(self):
        self.say()
        print("教学")
class Student(Person):
    def study(self):
        self.say()
        print("学习")

qtx = Teacher()
qtx.say()
qtx.teach()
xm = Student()
xm.say()
xm.study()

# 对象 是一种 类型： isinstance(对象,类型)
# 老师对象 是一种 老师类型
print(isinstance(qtx, Teacher)) # True
# 老师对象 是一种 人类型
print(isinstance(qtx, Person)) # True
# 老师对象 是一种 学生类型
print(isinstance(qtx, Student)) # False
# 人对象 是一种 学生类型
# print(isinstance(p, Student)) # False
# 类型 是一种 类型： issubclass(类型,类型)
# 老师类型 是一种 老师类型
print(issubclass(Teacher, Teacher)) # True
# 老师类型 是一种 人类型
print(issubclass(Teacher, Person)) # True
# 老师类型 是一种 学生类型
print(issubclass(Teacher, Student)) # False
# 人类型 是一种 学生类型
print(issubclass(Person, Student)) # False
# 是的关系
# 老师对象的类型 是 老师类型
print(type(qtx) == Teacher) # True
# 老师对象的类型 是 人类型
print(type(qtx) == Person) # False