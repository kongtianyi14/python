"""
    字典:(1) 由一系列键值对组成的可变散列容器。
        (2) 散列：对键进行哈希运算，确定在内存中的存储位置，每条数据存储无先后顺序。
        (3) 键必须惟一且不可变(字符串/数字/元组)，值没有限制。
    元组：(1) 由一系列变量组成的不可变序列容器。
         (2) 不可变是指一但创建，不可以再添加/删除/修改元素。
"""
# 1. 创建
# -- { 键1:值1, 键2:值2 }
dict_wk = {"name": "悟空", "age": 25, "sex": "女"}
dict_bj = {"name": "八戒", "age": 26, "sex": "男"}
dict_xbl = {"name": "小白龙", "age": 23, "sex": "女"}
# -- dict( [( , ),( , )] )
# 列表转换为字典的格式要求：列表元素必须能够"一分为二"
list01 = ["八戒", ("ts", "唐僧"), [1001, "齐天大圣"]]
dict01 = dict(list01)
# 2. 添加 字典名[键] = 值
dict_wk["money"] = 100000
print(dict_wk) # {'name': '悟空', 'age': 25, 'sex': '女', 'money': 100000}
# 字典不能使用 索引 切片
# 3. 定位：字典名[键]
# -- 读取
print(dict_wk["name"])
# 注意：如果没有键则报错
# 解决：读取数据前,通过in判断.
if "money" in dict_wk:
    print(dict_wk["money"])
# -- 修改(与添加数据语法相同)
# 具有key为修改,没有key为添加
dict_wk["name"] = "空空"
print(dict_wk) # {'name': '空空', 'age': 25, 'sex': '女', 'money': 100000}
# 4. 删除 del 字典名[键]
del dict_wk["sex"]
print(dict_wk) # {'name': '空空', 'age': 25, 'money': 100000}
# 5. 遍历
# 方式1：for 键 in 字典名称
for key in dict_wk:
    print(key)
# 方式2：for 值 in 字典名称.values()
for value in dict_wk.values():
    print(value)
# 方式3：for 键,值 in 字典名称.items()
for key,value in dict_wk.items():
    print(key)
    print(value)
# 数据类型名称( ... )
#　[('name', '李佳豪'), ('age', 25), ('sex', '女')]
print(list(dict_wk.items())) # [('name', '空空'), ('age', 25), ('money', 100000)]