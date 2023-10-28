"""
    功能增加的思想
    ctrl + o


class A:
    def func01(self, obj):
        obj.func()  # 先确定用法


class Base:  # 隔离变化
    def func(self):  # 统一行为
        pass


class B(Base):
    def func(self):  # 后确定做法
        pass


class C(Base):
    def func(self):
        pass


a = A()
a.func01(B())
a.func01(C())
"""

# -------------架构师------------------
class Person:
    def __init__(self, name=""):
        self.name = name
    def go_to(self, vehicle):
        print("去东北")
        if isinstance(vehicle,Vehicle):# 车 是一种 交通工具
            vehicle.transport()
class Vehicle: # 接口
    def transport(self):
        pass
# -------------程序员------------------
class Car(Vehicle):
    #重写
    def transport(self):
        print("汽车在行驶")
class Airplane(Vehicle):
# 重写快捷键:ctrl + o
    def transport(self):
        print("飞机在飞行")
# -------------测试------------------
lz = Person("老张")
car = Car()
lz.go_to(car)
lz.go_to(Airplane())