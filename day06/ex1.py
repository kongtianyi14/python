"""
    list01 = [1,2,3,4,5,4,3,2,1]
    根据数量打印星星*
"""
list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# for i in list01:
#     print("*" * i)

for item in range(0, len(list01)):
    print("*" * list01[item])
