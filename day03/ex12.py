"""
    while
        延长程序的生命
        if 条件：
            break
"""
while True:
    sex = input("请输入性别:")
    if sex == "男":
        print("您好，先生")
    elif sex == "女":
        print("您好，女士")
    else:
        print("性别未知")
    w = input("输入Q继续:")
    if w != "Q":
        break
# 让下列代码重复执行，输入Q继续(不输入Q则退出)