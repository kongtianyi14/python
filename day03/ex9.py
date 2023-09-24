"""
    条件表达式
"""
if input("请输入性别:") == "男":
    value = 1
else:
    value = 0
print(value)
# 这个语句等同于
value = 1 if input("请输入性别:") == "男" else 0
# 条件表达式一般用于在判断条件过后，要对一个变量进行赋值操作
# 而且1、必须是if-else
#    2、必须是同一变量
print(value)