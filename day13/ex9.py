"""
    算数运算符 重写
            + 对应 __add__
        判断
            type() ==     
"""


# class Vector2:
#     def __init__(self, x, y):
#         """
#         二维向量
#         :param x:
#         :param y:
#         """
#
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "x是:%d,y是:%d" % (self.x, self.y)
#
#     def __add__(self, other):
#         return Vector2(self.x + other.x, self.y + other.y)
#
#
# v01 = Vector2(1, 2)
# v02 = Vector2(2, 3)
# print(v01 + v02)  # v01.__add__(v02)

class Vector2:
    def __init__(self, x, y):
        """
        二维向量
        :param x:
        :param y:
        """

        self.x = x
        self.y = y

    def __str__(self):
        return "x是:%d,y是:%d" % (self.x, self.y)

    # 之前的方法无法满足 向量与数值的相加
    def __add__(self, other):
        if type(other) == Vector2:
            x = self.x + other.x
            y = self.y + other.y
            return Vector2(x, y)
        else:
            x = self.x + other
            y = self.y + other
            return Vector2(x, y)

v01 = Vector2(1, 2)
v02 = Vector2(2, 3)
print(v01 + v02)  # v01.__add__(v02)
print(v01 + 10)