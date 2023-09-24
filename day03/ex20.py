"""
    range(开始，结束，间隔)
    不包含结束值
    不写间隔默认为1
    不写开始默认为0


在终端中累加 0 1 2 3
在终端中累加 2 3 4 5 6
在终端中累加 1 3 5 7
在终端中累加 8 7 6 5 4
在终端中累加 -1 -2 -3 -4 -5
"""
total = 0
# for i in range(0,4):
#     total += i
# print(total)


# for i in range(2,7):
#     total += i
# print(total)

# for i in range(1,9,2):
#     total += i
# print(total)

# for i in range(8,3,-1):
#     total += i
# print(total)


for i in range(-1, -6, -1):
    total += i
print(total)
