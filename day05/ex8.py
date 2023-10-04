"""
生成10-30之间能被3或5整除的数字
"""
# list01 = []
# for i in range(10,31):
#     list01.append(i)
# new_list = [item for item in list01 if item % 3 == 0 or item % 5 == 0]
# print(new_list)

list01 = []
for i in range(5,21):
    list01.append(i)#可以直接in range()
new_list = [item **2 for item in list01 ]
print(new_list)
