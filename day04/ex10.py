"""
    索引
        定位
"""
message = "我是花果山齐天大圣"
print(message[2]) # 花
print(message[-2]) # 大
print(len(message)) # 9
# 注意：索引不能越界IndexError
# print(message[99])
# print(message[-99])

"""
    切片
        定位多个元素
        容器[开始索引:结束索引:步长]
        注意：不包含结束
"""
message = "我是花果山齐天大圣"
print(message[2:5:1]) # 花果山
print(message[1: 5]) # 是花果山
print(message[2:-4]) # 花果山
print(message[:-4]) # 我是花果山
print(message[:]) # 我是花果山齐天大圣
print(message[-3:]) # 天大圣
print(message[:2]) # 我是
print(message[-2:]) # 大圣
print(message[-2: 3:-1]) # 大天齐山
print(message[1: 1]) # 空
print(message[2: 5:-1]) # 空
# 特殊:翻转
print(message[::-1]) # 圣大天齐山果花是我