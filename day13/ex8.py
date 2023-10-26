"""
    重写内置函数
        (1)定义：Python中，以双下划线开头、双下划线结尾的是系统定义的成员。我们可以在自定义类中进
                行重写，从而改变其行为。
        (2) __str__ 函数：将对象转换为字符串(对人友好的)
"""


class Person(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}的年龄是{self.age}"

    def __int__(self):
        return self.age
wk = Person("悟空", 26)
# <__main__.Person object at 0x7fbabfbc3e48>
# 悟空的年龄是26
print(wk)
# message = wk.__str__()
# print(message)
print(int(wk))

"""
直接打印商品对象: xx的编号是xx,单价是xx
直接打印敌人对象: xx的攻击力是xx,血量是xx
"""
class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}的编号是{self.cid},单价是{self.price}"

A = Commodity(1001,"A",100)
print(A)

class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    def __str__(self):
        return f"{self.name}的攻击力是{self.atk},血量是{self.hp}"