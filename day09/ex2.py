"""
传参说明：
不可变类型的数据传参时，函数内部不会改变原数据的值。
可变类型的数据传参时，函数内部可以改变原数据。
"""


# def func01(p1, p2, p3):
#     p1 = 100
#     p2 = 200
#     c.append(300)
#     return p1
#
#
# a = 10
# b = [20]
# c = [30]
# d = func01(a, b, c)
# print(a)
# print(b)
# print(c)
# print(d)


def func02(p1, p2, p3):
    p1 = 100
    p2 = 200
    p3.append(300)
    return p1


a = 10
b = [20]
c = [30]
d = func02(a, b, c)
print(a)
print(b)
print(c)
print(d)
