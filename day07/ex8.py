"""
自定义排序算法
"""
"""
list01 = [5,65,76,87,89,9]
从大到小
"""
list01 = [5, 65, 76, 87, 89, 9]
for r in range(len(list01) - 1):
    for i in range(r + 1, len(list01)):
        if list01[i] > list01[r]:
            list01[i], list01[r] = list01[r], list01[i]
print(list01)
"""
list02 = [54,56,76,7,89]
从小到大
"""
list02 = [54, 56, 76, 7, 89]
for r in range(len(list02) - 1):
    for i in range(r + 1, len(list02)):
        if list02[i] < list02[r]:
            list02[i], list02[r] = list02[r], list02[i]
print(list02)