"""
购物流程
"""
# 商品字典
dict_commodity_infos = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 80000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

# 订单列表
list_orders = [
]
while True:
    need = int(input("输入1购买，输入2结算。"))
    if need == 1:
        for key, value in dict_commodity_infos.items():
            print(f'商品编号{key},商品名称{value["name"]},商品单价{value["price"]}')
        while True:
            cid = int(input("请输入您需要的商品编号："))
            number = int(input("请输入您需要的商品数量："))
            if cid in dict_commodity_infos.keys():
                list_orders.append({"cid":cid,"count":number})
            else:
                print("输入的数字有误！")
                continue
            need1 = int(input("是否继续？1继续其他退出"))
            if need1 == 1:
                continue
            else:
                break
    elif need == 2:
        total = 0
        for i in list_orders:
            print("商品编号%d,购买数量%d" % (i["cid"], i["count"]))
            total += dict_commodity_infos[i["cid"]]["price"] * i["count"]
        payment = int(input(f"总价{total}元，请输入您的金额:"))
        if payment == total:
            print("购买成功！")
        else:
            print("购买失败！")
    else:
        print("输入的数字有误！")

#
# # 打印所有商品信息
# # 格式:商品编号xx，商品名称xx，商品单价xx
# # dict_commodity_infos = {
# #     1001:{"name" : "屠龙刀", "price": 10000},
# #     1002:{"name" :"倚天剑", "price" :10000},
# #     1003:{"name" : "金箍棒", "price": 52100},
# #     1004:{"name" : "口罩", "price" :20},
# #     1005:{"name" : "酒精", "price" :30}
# # }
# for key, value in dict_commodity_infos.items():
#     print("商品编号%d,商品名称%s,商品单价%d" % (key, value["name"], value["price"]))
#
# # 打印所有订单中的信息
# # 商品编号xx,购买数量xx
# # list_orders = [
# #     {"cid":1001,"count":1},
# #     {"cid":1002,"count":3},
# #     {"cid":1005,"count":2},
# # ]
# for i in list_orders:
#     print("商品编号%d,购买数量%d" % (i["cid"], i["count"]))
#
# # 打印所有订单中的商品信息
# # 格式：商品名称：xx，商品单价：xx，商品数量：xx。
# for i in list_orders:
#     print("商品名称：%s，商品单价：%d，商品数量：%d" % (dict_commodity_infos[i["cid"]]["name"],
#                                        dict_commodity_infos[i["cid"]]["price"], i["count"]))
#
# # 查找数量最多的订单
# most = list_orders[0]["count"]
# pos = 0
# for i in range(1, len(list_orders)):
#     if list_orders[i]["count"] > most:
#         most = list_orders[i]["count"]
#         pos = i
# # print(list_orders[pos]["cid"])
# # print(most)
# print("数量最多的订单为%s,数量为%s" % (list_orders[pos]["cid"], most))
#
# # 根据购买数量对订单列表降序排列
# for r in range(len(list_orders) - 1):
#     for i in range(r + 1, len(list_orders)):
#         if list_orders[i]["count"] > list_orders[r]["count"]:
#             list_orders[i],list_orders[r] = list_orders[r] ,list_orders[i]
# print(list_orders)
#
#
# #创建函数
# # 打印所有商品信息
# # 格式:商品编号xx，商品名称xx，商品单价xx
# # dict_commodity_infos = {
# #     1001:{"name" : "屠龙刀", "price": 10000},
# #     1002:{"name" :"倚天剑", "price" :10000},
# #     1003:{"name" : "金箍棒", "price": 52100},
# #     1004:{"name" : "口罩", "price" :20},
# #     1005:{"name" : "酒精", "price" :30}
# # }
# def print_message():
#     # global dict_commodity_infos
#     for key, value in dict_commodity_infos.items():
#         print("商品编号%d,商品名称%s,商品单价%d" % (key, value["name"], value["price"]))
# print_message()






