"""
    累加10 -- 60之间，个位不是3/5/8的整数和。
"""
value = 0
for item in range(10,61):
    A = item % 10
    if A == 3 or A == 5 or A == 8:
        continue
    value += item
print(value)