"""
在终端中输入任意整数，计算累加和.
"1234" -> "1" -> 累加 1
效果：
请输入一个整数:12345
累加和是 15
"""
number = input("输入任意整数:")
total = 0
for item in number:
    total += int(item)
print("累加和是" + str(total))
