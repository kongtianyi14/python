"""
列表中整数不是5和3
list = [25,63,27,75,70,83,27]
"""
list01 = [25, 63, 27, 75, 70, 83, 27]
result = []
for i in list01:
    if i % 10 != 3 and i % 10 != 5:
        result.append(i)
print(result)
