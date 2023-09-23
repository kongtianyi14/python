"""
        del 删除语句
        del 变量名1，变量名2
"""
name_of_beijing,region = "北京","市"
name_of_beijing_region = name_of_beijing + region
region = "省"
print(name_of_beijing_region)
del name_of_beijing
print(name_of_beijing_region)
# 想表达的是删除和修改之后的数据通常来说是不会影响之前已经改变的数据
