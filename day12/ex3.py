class CommodityModel:
    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid

class CommodityView:
    def __init__(self):
        self.controller = CommodityController()

    def display_menu(self):
        print("1键录入商品信息")
        print("2键显示商品信息")
        print("3键删除商品信息")
        print("4键修改商品信息")

    def select_menu(self):
        item = input("请您输入选项:")
        if item == "1":
            self.input_commodity_info()
        elif item == "2":
            self.display_commoditys()

    def input_commodity_info(self):
        com = CommodityModel()
        com.name = input("请输入人商品名称:")
        com.price = input("请输入人商品价格:")
        self.controller.add_commodity(com)
        #com.cid由控制器赋值

    def display_commoditys(self):
        for item in self.controller.list_commodity:
            print(f"{item.name}的编号是{item.cid}")

class CommodityController:
    start_cid = 1001
    def __init__(self):
        self.list_commodity = []

    @classmethod
    def cid_selfup(cls,new_com):
        new_com.cid = cls.start_cid
        cls.start_cid += 1

    def add_commodity(self, new_com):
        #自增长
        CommodityController.cid_selfup(new_com)
        self.list_commodity.append(new_com)

A = CommodityView()
while True:
    A.display_menu()
    A.select_menu()