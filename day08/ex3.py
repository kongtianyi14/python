# 崇尚小而精，拒绝大而全
"""
创建计算治愈比例的函数
confirmed = int(input("请输入确诊人数:"))
cure = int(input("请输入治愈人数:"))
cure_rate = cure / confirmed * 100
print("治愈比例为" + str(cure_rate) + "%")
"""
def cure_rate(a,b):
    c = b / a * 100
    return str(c)+"%"

confirmed = int(input("请输入确诊人数:"))
cure = int(input("请输入治愈人数:"))
result = cure_rate(confirmed,cure)
print(result)