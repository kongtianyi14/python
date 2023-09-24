"""
    在终端中输入整数
    打印正数、 负数、零
"""
num = int(input("请输入整数:"))
if num > 0:
    print("正数")
elif num < 0:
    print("负数")
else:
    print("零")
