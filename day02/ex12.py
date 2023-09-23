"""
录入1234，打印1+2+3+4结果
效果：
请输入四位整数：1234
结果是：10
"""
num = int(input("请输入四位整数："))
a = num // 1000
b = num % 1000 // 100
c = num % 1000 % 100 // 10
d = num % 10
result = a + b + c + d
print("结果是：" + str(result))
