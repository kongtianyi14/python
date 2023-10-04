"""
    列表与字符串的转换
"""
#列表转化为字符串
# list01 = ["a","b","c"]
# reslut = "-".join(list01)#连接
# print(reslut)

# reslut = ""
# for i in range(10):
#     reslut += str(i)
# print(reslut)

reslut = []
for i in range(10):
    reslut.append(str(i))
print("".join(reslut))

#字符串转换为列表
list01 = "a,b,c".split(",")
print(list01)

# to have a government that is of people by people for people
#将上面这句话进行反转
list01 = "to have a government that is of people by people for people".split(" ")
list02 = list01[::-1]
print(" ".join(list02))

