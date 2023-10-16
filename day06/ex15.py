"""
"经理" = "a","b","c"
"技术" = "a","b","d","e"
"""
# set_man = {"a","b","c"}
# set_tec = {"a","b","d","e"}
# print(set_man & set_tec)
# print(set_man - set_tec)
# print(set_tec - set_man)
# print(set_tec ^ set_man)
# set_total = set_man | set_tec
# count = 0
# for i in set_total:
#     count += 1
# print(count)

dict01 = {
    "经理" : {"a","b","c"},
    "技术" : {"a","b","d","e"}
}
print(dict01["经理"] & dict01["技术"])
print(dict01["经理"] - dict01["技术"])
print(dict01["技术"] - dict01["经理"])
print(dict01["技术"] ^ dict01["经理"])
print(len(dict01["技术"] | dict01["经理"]))


