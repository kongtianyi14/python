"""
在终端中输入课程阶段数,显示课程名称
效果：
输入              输出
1              Python语言核心编程
2              Python高级软件技术
3              Web 全栈
4              人工智能
"""
num = int(input("输入课程阶段数:"))
if num == 1:
    print("Python语言核心编程")
elif num == 2:
    print("Python高级软件技术")
elif num == 3:
    print("Web 全栈")
elif num == 4:
    print("人工智能")
else:
    print("您的输入有错误！")
