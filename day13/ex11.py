"""
    iadd与add的区别
    add 返回的是一个新的地址的类型
    idd 返回的是在本身做出修改的类型
"""

class Vector2:
    """
    二维向量
`    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x是:%d,y是:%d" % (self.x, self.y)

    # + 创建新
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    # += 在原有基础上修改(自定义类属于可变对象)
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

v01 = Vector2(1, 2)
v02 = Vector2(2, 3)
print(id(v01))
v01 += v02
print(id(v01))
print(v01)