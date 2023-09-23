"""
匀变速直线运动的速度与位移公式：
位移 = 初速度 × 时间 + 加速度 * 时间的平方 / 2
已知(在终端中录入)：位移、时间、初速度
计算：加速度
效果：
请输入距离：100
请输入初速度：6
请输入时间：10
加速度是：0.8
"""
distance = float(input("请输入距离："))
speed = float(input("请输入初速度："))
time = float(input("请输入时间："))
acc = 2*(distance - speed * time)/time **2
print("加速度是："+str(acc))