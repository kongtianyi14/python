"""
     汇率转换器
"""
# 1.获取数据
USD = float(input("请输入美元数额："))
# 2.逻辑计算:美元 * 6.405
CNY = USD * 6.405
# 3.显示结果
print(str(USD) + "美元 =" + str(CNY) + "人民币")
