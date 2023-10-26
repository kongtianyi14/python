class CommodityModel:
    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid

    def __str__(self):
        return f"{self.name}的编号是{self.cid}"

    def __eq__(self, other):
        return self.cid == other.cid

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
        elif item == "3":
            self.delete_commoditys()
        elif item == "4":
            self.change_commoditys()

    def input_commodity_info(self):
        new_com = CommodityModel()
        new_com.name = input("请输入人商品名称:")
        new_com.price = int(input("请输入人商品价格:"))
        # cid由Controller决定
        self.controller.add_commodity(new_com)

    def display_commoditys(self):
        for item in self.controller.list_commodity:
            # print(f"{item.name}的编号是{item.cid}")
            print(item)

    def delete_commoditys(self):
        del_cid = int(input("请输入您要删除的cid:"))
        if self.controller.delete_commoditys(del_cid):
            print("删除成功")
        else:
            print("删除失败")

    def change_commoditys(self):
        change_com = CommodityModel()
        change_com.cid = int(input("请输入要修改的商品cid："))
        change_com.name = input("请输入修改后的商品名字：")
        change_com.price = int(input("请输入修改后的商品价格："))
        if self.controller.change_commoditys(change_com):
            print("修改成功")
        else:
            print("修改失败")


class CommodityController:
    start_cid = 1001

    @classmethod
    def cid_selfup(cls, new_com):
        new_com.cid = CommodityController.start_cid
        CommodityController.start_cid += 1

    def __init__(self):
        self.list_commodity = []

    def add_commodity(self, new_com):
        self.cid_selfup(new_com)
        self.list_commodity.append(new_com)

    def delete_commoditys(self, del_cid):
        # for i in range(len(self.list_commodity)):
        #     if self.list_commodity[i].cid == del_cid:
        #         del self.list_commodity[i]
        #         return True
        # return False
        # for item in self.list_commodity:
        #     if item.cid == del_cid:
        #         self.list_commodity.remove(item)
        #         return True
        # return False
        del_com = CommodityModel(cid = del_cid)
        if del_com in self.list_commodity:
            self.list_commodity.remove(del_com)
            return True
        return False

    def change_commoditys(self, change_com):
        for item in self.list_commodity:
            if item.cid == change_com.cid:
                item.name = change_com.name
                item.price = change_com.price
                return True
        return False


view = CommodityView()
while True:
    view.display_menu()
    view.select_menu()
