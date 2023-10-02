"""
# 需求：累加1-100之间能被3整除的数字
# 思想：不满足条件跳过,否则累加.
"""
sum_value = 0
for item in range(1, 101):
    if item % 3 != 0:
        continue
    sum_value += item
print(sum_value)
