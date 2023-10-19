# def total_second(huor = 0,minute = 0,second = 0):#默认值
#     pass
#
#
# total_second()

def func01(*p): #多个位置实参元组
    print(p)
def func02(**p): #多个位置实参元组
    print(p)
func01(1)
func01(1)
func01(1,2,3)

func02(a =1,b=2) #不支持位置实参字典

#完成数字的累乘
def x_number(*p):
    total = 1
    for i in p:
        total *= i
    return total

print(x_number(1,2,3,4,5,6,7,8,9,10))