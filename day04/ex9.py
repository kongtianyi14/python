"""
获取一个整数
以他为边长打印一个用$代表的一个单位的正方形
"""
side = int(input("请输入一个整数："))
# print("$" * side)
# for item in range(0, side - 2):
#     # print("$" + " " * (side - 2) + "$")
#     print("$%s$"%(" "*(side -2 )))
# print("$" * side)

for item in range(0, side):
    if item == 0 or item == side -1:
        print("$" * side)
    else:
        print("$%s$" % (" " * (side - 2)))

