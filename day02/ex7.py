"""
    在终端中输入商品单价、购买的数量和支付金额。计算应该找回多少钱。
"""
price = float(input("请输入商品的单价:"))
num = float(input("请输入商品的数量:"))
pay = float(input("请输入商品的支付的金额:"))
back = pay - (price * num)
print("应该找回：" + str(back))
