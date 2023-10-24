"""
    跨类调用
"""
# 写法1：直接创建对象
# 语义：老张每次创建一辆新车去
class Person:
    def __init__(self, name=""):
        self.name = name
    def go_to(self,position):
        print("去",position)
        car = Car()
        car.run()
class Car:
    def run(self):
        print("跑喽～")
lz = Person("老张")
lz.go_to("东北")
# 写法2：在构造函数中创建对象
# 语义：老张开自己的车去
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()
    def go_to(self,position):
        print("去",position)
        self.car.run()
class Car:
    def run(self):
        print("跑喽～")
lz = Person("老张")
lz.go_to("东北")

# 方式3：通过参数传递
# 语义：老张用交通工具去
class Person:
    def __init__(self, name=""):
        self.name = name
    def go_to(self,vehicle,position):
        print("去",position)
        vehicle.run()
class Car:
    def run(self):
        print("跑喽～")
lz = Person("老张")
benz = Car()
lz.go_to(benz,"东北")