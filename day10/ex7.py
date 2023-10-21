class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


class Orders:
    def __init__(self, cid, count=1):
        self.cid = cid
        self.count = count


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30)
]

list_orders = [
    Orders(1001),
    Orders(1002,3),
    Orders(1003,2),
]


def print_single_commodity(commodity):
    print(f"编号:{commodity.cid},商品名称:{commodity.name},商品单价:{commodity.price}")


def print_commodity_infos():
    for commodity in list_commodity_infos:
        print_single_commodity(commodity)


def print_price_in_2w():
    for commodity in list_commodity_infos:
        if commodity.price < 20000:
            print_single_commodity(commodity)


def print_order_infos():
    for order in list_orders:
        for commodity in list_commodity_infos:
            if order.cid == commodity.cid:
                print(f"商品名称{commodity.name},商品单价:{commodity.price},数量{order.count}.")
                break  # 跳出内层循环

def commodity_max_by_price():
    max_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if max_value.price < list_commodity_infos[i].price:
            max_value = list_commodity_infos[i]
    return max_value

def descending_order_by_price():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r].price < list_commodity_infos[c].price:
                list_commodity_infos[r], list_commodity_infos[c] =list_commodity_infos[c], list_commodity_infos[r]