"""
    输入一个整数，如果是奇数就给变量state“奇数”否则“偶数”
"""

#符合条件表达式的运用
state = "奇数" if int(input("请输入一个整数：")) % 2 == 1 else "偶数"
print(state)