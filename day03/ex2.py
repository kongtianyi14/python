"""
    语句
        选择语句
        if 条件1:
            语句块1
        elif 条件2:
            语句块2
        else:
            语句块3
"""
# #调试！：让程序中断，逐行语句执行，审查流程和变量的取值
# 步骤：
# 1、加断点
# 2、开始调试 debug  shift+F9
sex = input("请输入性别:")
if sex == "男":
    print("您好，先生")
elif sex == "女":
    print("您好，女士")
else:
    print("性别未知")
