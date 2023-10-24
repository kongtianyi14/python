"""
    ICBC
"""
class ICBC:
    total_money =1000000
    def __init__(self, name="", money=0):
        self.name = name
        self.money = money
        ICBC.total_money -= self.money

    @classmethod
    def print_total_money(cls):
        print("总行的钱",cls.total_money)
cheng_du = ICBC("成都支行",10000)
# print(f"总行金额:{ICBC.total_money}")
ICBC.print_total_money()
chong_qing= ICBC("重庆支行",10000)
print(f"总行金额:{ICBC.total_money}")



# class MyClass:
#     data02 = 20
#     def __init__(self):
#         self.data01 = 10
#         self.data01 += 1
#         MyClass.data02 += 1
#
# m1=MyClass()
# m2=MyClass()
# m3=MyClass()
# print(m3.data01)
# print(MyClass.data02)