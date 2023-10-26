"""
    练习：创建颜色类，数据包含r、g、b、a，实现颜色对象累加。
"""


class Color:
    def __init__(self, r=0, g=0, b=0, a=0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return f"r = {self.r} g = {self.g} b = {self.b} a = {self.a}"

    def __add__(self, other):
        if type(other) == Color:
            r = self.r + other.r
            g = self.g + other.g
            b = self.b + other.b
            a = self.a + other.a
            return Color(r, g, b, a)
        else:
            r = self.r + other
            g = self.g + other
            b = self.b + other
            a = self.a + other
            return Color(r, g, b, a)