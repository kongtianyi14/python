"""
古代的秤，一斤十六两。在终端中获取两，计算几斤零几两。
效果：
请输入总两数：100
结果为：6斤4两
"""
total = int(input("请输入总两数："))
result01 = total // 16
result02 = total % 16
print("结果为：" + str(result01) + "斤" + str(result02) + "两")
print("结果为：%s斤%s两"%(result01, result02))
