"""
程序产生1个,1到100之间的随机数。
让玩家重复猜测,直到猜对为止。
每次提示：大了、小了、恭喜猜对了,总共猜了多少次。
效果：
请输入要猜的数字:50
大了
请输入要猜的数字:25
小了
请输入要猜的数字:35
大了
请输入要猜的数字:30
小了
请输入要猜的数字:32
恭喜猜对啦,总共猜了5次



# 准备一个随机数工具
import random
#生成一个随机数1~100
random_number = random.randint(1,100)
"""
# 准备一个随机数工具
import random

# 生成一个随机数1~100
random_number = random.randint(1, 100)
count = 0
while True:
    guess_number = int(input("请输入要猜的数字:"))
    count += 1
    if guess_number != random_number:
        if guess_number < random_number:
            print("小了")
        elif guess_number > random_number:
            print("大了")
    else:
        break
print("恭喜猜对啦,总共猜了" + str(count) + "次")

# while 条件:
#     内容
#     if 条件:
#         break
# else:
#     "失败"
#
# 那么导致失败的原因有两个1、while内部的条件2、while开头时的条件
# （特别注意的是如果执行了else，就可以确认是通过while开头时的条件
# 结束循环的，因为通过break结束的语句，不会执行后面的else）