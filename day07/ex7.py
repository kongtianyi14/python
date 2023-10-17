"""
dict_travel_info = {
    "北京":{
        "景区":["长城","故宫"],
        "美食":["烤鸭","豆汁焦圈","炸酱面"]
    }
    "四川":{
        "景区":["九寨沟","峨眉山"],
        "美食":["火锅","兔头"]
    }
}
"""
dict_travel_info = {
    "北京":{
        "景区":["长城","故宫"],
        "美食":["烤鸭","豆汁焦圈","炸酱面"]
    },
    "四川":{
        "景区":["九寨沟","峨眉山"],
        "美食":["火锅","兔头"]
    }
}
#打印北京的第一个景区
print(dict_travel_info["北京"]["景区"][0])
#打印四川的第二个美食
print(dict_travel_info["四川"]["美食"][1])
#所有城市
for key in dict_travel_info.keys():
    print(key)
#北京所有美食
for i in dict_travel_info["北京"]["美食"]:
    print(i)
#所有城市的所有所有美食
for values in dict_travel_info.values():
    for i in values["美食"]:
        print(i)