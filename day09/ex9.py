"""
    函数参数
        实际参数
            位置参数
            关键字参数
        形式参数
            位置参数
            默认参数
            星号元组
            双星号字典
            星号元组,位置参数
            星号元组,默认参数
            主参，*，副参
"""


def func01(*args, p):
    print(args)
    print(p)

def fun02(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)
list01 = [10,20,30]
# fun02(list01)  会报错
fun02(*list01)
tuple01 = (10,20,30)
fun02(*tuple01)
name = "孙悟空"
fun02(*name)
dict01 = {"p2":2,"p1": 1,"p3" : 3}
fun02(*dict01)#传键
fun02(**dict01)#传参
