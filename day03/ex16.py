"""
一张纸的厚度是0.01毫米
请计算，对折多少次超过珠穆朗玛峰(8844.43米)
思路:
数据：厚度、高度、次数
算法：厚度*=2
"""
mountain_high = 8844.43
high = 0.00001
count = 0
while high < mountain_high:
    high *= 2
    count += 1
    print("这是第" + str(count) + "次对折，高度为" + str(high / 100) + "米")
print(count)
