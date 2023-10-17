"""
数字在列表中的最大值
[170, 160, 180, 165]
"""
list01 = [170, 160, 180, 165]
Max = list01[0]
for i in range(1,len(list01)):
    if list01[i] > Max:
        Max = list01[i]
print(Max)
print(max(list01))