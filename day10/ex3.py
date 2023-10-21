"""
    练习：创建手机类，实例化两个对象并调用其函数，最后画出内存图。
    数据：品牌、价格、颜色
    行为：通话
"""


class Mobilephone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print(self.brand + "在通话")

Apple = Mobilephone("iphone15 proMax", 12999, "black")
Huawei = Mobilephone("Mate60", 9999, "black")
print(Apple.brand)
Apple.call()



