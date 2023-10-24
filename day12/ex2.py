"""
创建对象计数器，统计结构函数执行的次数，使用类变量实现
"""


class Wife:
    total_count = 0
    def __init__(self, name=""):
        self.name = name
        Wife.total_count += 1

    @classmethod
    def print_count(cls):
        print(f"总共娶了{cls.total_count}个老婆")

w1 = Wife("1")
Wife.print_count()