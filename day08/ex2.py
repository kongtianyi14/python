"""
    函数
    返回值 return 后面不执行了
    崇尚小而精，拒绝大而全
"""
# def 函数名(形式参数):
#   函数体

"""
打印列表
list01 = [5,546,6,56,76,]
list02 = [7,6,879,9,909]
"""


def dl(name):
    for i in name:
        print(i, end="\t")


list01 = [5, 546, 6, 56, 76, ]
list02 = [7, 6, 879, 9, 909]

dl(list01)
dl(list02)
print()

"""
创建函数，在终端中打印矩形
"""


def print_jx():
    length = int(input("请输入长："))
    width = int(input("请输入宽："))
    # print("*" * length)
    # for i in range(width-2):
    #     print("*" + " "* (length-2) + "*")
    # print("*" * length)
    for raw in range(width):
        if raw == 0 or raw == (width - 1):
            print("*" * length)
        else:
            print("*" + " " * (length - 2) + "*")


print_jx()


def func04():


    while True:
        while True:
            while True:
# break 只能退出一层循环
                print("循环体")
                return
func04()
