data01 = ["悟空"]
data02 = data01
data01 = "孙悟空"
print(data02)

data03 = {"name":"悟空"}
data04 = data03
data04["name"] = "孙悟空"
print(data03["name"])

data05 = [{"name":"悟空"}]
data06 = data05[:]
data05[0]["name"] = "孙悟空"
print(data06)

"""
删除元素，建议倒序删除
"""
# for i in range(len(lis01)-1,-1,-1):