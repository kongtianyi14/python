"""
在终端中录入省份，不能录入重复，直到输入空字符串为止
"""
set01 = set()
while True:
    prevince = input("请输入需要录入的省份：")
    if prevince == "":
        break
    else:
        set01.add(prevince)
print(set01)