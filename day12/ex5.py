"""
    属性 -- 原理
        保护类中的数据在有效范围内
        实例变量和方法的关系
"""


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.set_age(age)
        self.age = age

    def set_age(self, value):
        if value > 80:
            value = 80
        elif value < 20:
            value = 20
        self.__age = value

    def get_age(self):
        return self.__age

    age = property(get_age,set_age)

a_ke = Wife("阿珂",100)