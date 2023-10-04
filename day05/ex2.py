"""
    小游戏
    本金10000，投色子小游戏
"""
import random

money = 10000
while True:
    if money <= 0:
        print("您的赌资已经用光，欢迎下次光临!")
        break
    gamble = int(input("这次赌注为多少:"))
    if gamble > money:
        print("您的赌注不能大于本金")
        continue
    else:
        A = random.randint(1, 6)
        print(f"您摇出了{A}点")
        B = random.randint(1, 6)
        print(f"您摇出了{B}点")
        if A > B:
            print("恭喜您，这局你赢了!")
            money += gamble
        elif A < B:
            print("真遗憾，这局你输了!")
            money -= gamble
        else:
            print("平局，这把流局。")
    print(f"本金还剩{money}")
