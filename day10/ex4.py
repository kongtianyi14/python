"""
    语法
        a. 定义：对象.变量名
        b. 调用：对象.变量名
"""
# class Wife:
#     pass
#
# jian_ning = Wife()
# jian_ning.name = "公主"#创建
class Wife:
    def __init__(self, name):
        self.name = name
def print_self(self):
    print("我是：", self.name)
lili = Wife("丽丽") # dict01 = {"name":"丽丽"}
lili.name = "莉莉" # dict01["name"] = "莉莉"
print(lili.name) # print(dict01["name"])
lili.print_self()
print(lili.__dict__) # {"name":"丽丽"}
"""
# 支持动态创建类成员
# 类中的成员应该由类的创造者决定
class Wife:
    pass
w01 = Wife()
w01.name = "莉莉"
print(w01.name)#对象.变量名
"""
"""
# 实例变量的创建要在构造函数中__init__
class Wife:
    def set_name(self,name):
        self.name = name
w01 = Wife()
w01.set_name("丽丽")
print(w01.name)
"""
