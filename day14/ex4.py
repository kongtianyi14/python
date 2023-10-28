"""
    创建一个图形管理器
    --记录多种图形（圆形、矩形）
    --提供计算面积的方法
    要求：增加行的图形不影响图形管理器
"""


class Graphic:
    def __init__(self):
        self.__list_graphicals = []

    def add_graphical(self, graphical):
        if isinstance(graphical, Graphical):
            self.__list_graphicals.append(graphical)

    def calculate_area(self):
        for item in self.__list_graphicals:
            print(item.calculate_area())


class Graphical:
    def calculate_area(self):
        pass


# -----------------------------------------------------------
class Circular(Graphical):
    def __init__(self, r=0):
        self.r = r

    def calculate_area(self):
        return 3.14 * (self.r ** 2)


class Rectangle(Graphical):
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
#----------------------------------------------------------------------
A = Graphic()
test01 = Circular(2)
test02 = Rectangle(2,3)
A.add_graphical(test01)
A.add_graphical(test02)
A.calculate_area()