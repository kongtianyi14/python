"""
    列表推导式嵌套
"""
list01 = [1,2,3,4]
list02 = [5,6,7,8]
list_new = []
for r in list01:
    for c in list02:
        list_new.append((r,c))
print(list_new)

list_new = [(r,c) for r in list01 for c in list02]
print(list_new)