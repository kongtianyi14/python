"""
    姓名列表:["张无忌","赵敏","周芷若"]
    房间列表:[101,102,103]
    两个列表合并成一个字典
"""
list01 = ["张无忌","赵敏","周芷若"]
list02 = [101,102,103]
dict_id = {}
for i in range(len(list01)):
    dict_id[list01[i]] = list02[i]
print(dict_id)

# 推导式

dict_id = {list01[i] :list02[i] for i in range(len(list01))}
print(dict_id)
"""
    姓名列表:["张无忌","赵敏","周芷若"]
    房间列表:[101,102,103]
    两个列表合并成一个字典
    并将键值对的位置调换
"""

new_dict = {}
for k,v in dict_id.items():
    new_dict[v] = k
print(new_dict)

list01 = ["张无忌","赵敏","周芷若"]
list02 = [101,102,103]
dict_id = {}
for i in range(3):
    dict_id[list02[i]] = list01[i]
print(dict_id)

