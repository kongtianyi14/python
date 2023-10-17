"""
"于谦":["抽烟","喝酒","烫头"]
"郭德纲":["说","学","逗","唱"]
"""
dict_hobbies = {
    "于谦":["抽烟","喝酒","烫头"],
    "郭德纲":["说","学","逗","唱"]
}
#打印于谦的爱好
for values in dict_hobbies["于谦"]:
    print(values)
#删除
# dict_hobbies["于谦"].remove("抽烟")
#计算郭德纲的所有爱好数量
print(len(dict_hobbies["郭德纲"]))

#打印所有人
for item in dict_hobbies.keys():
    print(item)

# dict_hobbies["大爷"] = dict_hobbies["于谦"]
# del dict_hobbies["于谦"]
# print(dict_hobbies)