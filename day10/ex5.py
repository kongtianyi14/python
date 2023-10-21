"""
    练习1：创建狗类，实例化两个对象并调用其函数，画出内存图。
    数据：品种、昵称、身长、体重
    行为：吃(体重增长1)
"""


class Dog:
    def __init__(self, kind, name, length, weight):
        self.kind = kind
        self.name = name
        self.length = length
        self.weight = weight

    def eat(self):
        self.weight += 1

bozai = Dog("泰迪","波仔","70cm",2.6)
bozai.eat()
print(bozai.weight)