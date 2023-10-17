"""
双色球：
红色：6个 1--33之间的整数 不能重复
蓝色：1个 1--16之间的整数
1）随机产生一注彩票
2）在终端录入一注彩票
"""
import random
list_tickt = []
while len(list_tickt) < 6:
    number = random.randint(1,33)
    if number in list_tickt:
        continue
    else:
        list_tickt.append(number)
list_tickt.append(random.randint(1,16))
print(list_tickt)

list_tickt01 = []
while len(list_tickt01) < 6:
    number = int(input(f"请输入第{len(list_tickt01) + 1}号球的数字："))
    if number in list_tickt01:
        print("号码已经存在")
        continue
    elif number < 1 or number > 33:
        print("号码超出范围")
        continue
    else:
        list_tickt01.append(number)

while len(list_tickt01) < 7:
    number = int(input(f"请输入第{len(list_tickt01) + 1}号球的数字："))
    if number < 1 or number > 16:
        print("号码超出范围")
        continue
    else:
        list_tickt01.append(number)
print(list_tickt01)