"""
在终端中输入一个疫情确诊人数再录入一个治愈人数，打印治愈比例
格式：治愈比例为xx%
效果：
请输入确诊人数：500
请输入治愈人数：495
治愈比例为99.0%
"""
ill_num = int(input("请输入确诊人数："))
cover_num = int(input("请输入治愈人数："))
rate = cover_num / ill_num * 100
print("治愈比例为" + str(rate) + "%")
