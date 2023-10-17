"""
颜色rgba a是透明
"""
color = input("请输入颜色（RGBA）:")
# list01 = [("R" , "红色"),("G" , "绿色"),("B" , "蓝色"),("A" , "透明")]
dict_color = dict([("R" , "红色"),("G" , "绿色"),("B" , "蓝色"),("A" , "透明")])
# dict_color = {
#     "R" : "红色",
#     "G" : "绿色",
#     "B" : "蓝色",
#     "A" : "透明"
# }
print(dict_color)
print(dict_color[color])
