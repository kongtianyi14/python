"""
商品信息
"""
# 商品字典
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30}
}

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]

# 打印所有商品信息
# 格式:商品编号xx，商品名称xx，商品单价xx
# dict_commodity_infos = {
#     1001:{"name" : "屠龙刀", "price": 10000},
#     1002:{"name" :"倚天剑", "price" :10000},
#     1003:{"name" : "金箍棒", "price": 52100},
#     1004:{"name" : "口罩", "price" :20},
#     1005:{"name" : "酒精", "price" :30}
# }
for key, value in dict_commodity_infos.items():
    print("商品编号%d,商品名称%s,商品单价%d" % (key, value["name"], value["price"]))

# 打印所有订单中的信息
# 商品编号xx,购买数量xx
# list_orders = [
#     {"cid":1001,"count":1},
#     {"cid":1002,"count":3},
#     {"cid":1005,"count":2},
# ]
for i in list_orders:
    print("商品编号%d,购买数量%d" % (i["cid"], i["count"]))

# 打印所有订单中的商品信息
# 格式：商品名称：xx，商品单价：xx，商品数量：xx。
for i in list_orders:
    print("商品名称：%s，商品单价：%d，商品数量：%d" % (dict_commodity_infos[i["cid"]]["name"],
                                       dict_commodity_infos[i["cid"]]["price"], i["count"]))

# 查找数量最多的订单
most = list_orders[0]["count"]
pos = 0
for i in range(1, len(list_orders)):
    if list_orders[i]["count"] > most:
        most = list_orders[i]["count"]
        pos = i
# print(list_orders[pos]["cid"])
# print(most)
print("数量最多的订单为%s,数量为%s" % (list_orders[pos]["cid"], most))

# 根据购买数量对订单列表降序排列
for r in range(len(list_orders) - 1):
    for i in range(r + 1, len(list_orders)):
        if list_orders[i]["count"] > list_orders[r]["count"]:
            list_orders[i],list_orders[r] = list_orders[r] ,list_orders[i]
print(list_orders)


#创建函数
# 打印所有商品信息
# 格式:商品编号xx，商品名称xx，商品单价xx
# dict_commodity_infos = {
#     1001:{"name" : "屠龙刀", "price": 10000},
#     1002:{"name" :"倚天剑", "price" :10000},
#     1003:{"name" : "金箍棒", "price": 52100},
#     1004:{"name" : "口罩", "price" :20},
#     1005:{"name" : "酒精", "price" :30}
# }
def print_message():
    # global dict_commodity_infos
    for key, value in dict_commodity_infos.items():
        print("商品编号%d,商品名称%s,商品单价%d" % (key, value["name"], value["price"]))
print_message()






