"""
小球从100m的高空坠落，每次回弹下落高度的1/2
且最小的下落高度为0.01m
问多少次弹起
全程移动了多少米
"""
total_bound = 0
total_distance = 100
hight = 100
while hight / 2 > 0.01:
    total_bound += 1
    hight /= 2
    total_distance += hight * 2
print(f"弹起{total_bound}次")
print(f"全程{total_distance:.2f}米")
