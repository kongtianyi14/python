"""
    在终端中录入疫情地区的名字直到录入空字符串位置
    如果录入相同的 则不再添加
    最后倒序打印地区
"""
result = []
while True:
    region = input("请输入疫情地区：")
    if region == "":
        break
    if region in result:
        print("已经存在该地区")
        continue
    else:
        result.append(region)
print(result[::-1])
