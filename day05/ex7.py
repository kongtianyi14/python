"""
    列表的推导式
"""
#将大于10的数存入另外一个列表
list01 = [4,54,65,67,78,8,9]
# new_list = []
# for item in list01:
#     if item > 10:
#         new_list.append(item)
# print(new_list)

# new_list=[item for item in list01 if item > 10]
# print(new_list)

#将所有数的个位存入另外一个列表
new_list = [item % 10 for item in list01]
print(new_list)