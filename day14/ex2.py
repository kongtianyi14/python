"""
    手雷爆炸，可能伤害敌人（头顶爆字）或者玩家碎屏
"""


# class Grenade:
#     def attack(self,target):
#         target.damage()
#
# class Target:
#     def damage(self):
#         pass
#
# class Enemy(Target):
#     def damage(self):
#         print("头顶爆字")
#
# class Player(Target):
#     def damage(self):
#         print("碎屏")
#
# A = Grenade()
# B = Player()
# A.attack(B)

class Grenade:
    def __init__(self, atk=0):
        self.atk = atk

    def explode(self, target):
        print("爆炸")
        target.damage(self.atk)

class Target:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print(self.hp)


class Player(Target):
    # def __init__(self, hp=0):
    #     self.hp = hp

    def damage(self, value):
        print("碎屏")
        # self.hp -= value
        super().damage(value)


class Enemy(Target):
    # def __init__(self, hp=0):
    #     self.hp = hp

    def damage(self, value):
        print("头顶爆字")
        # self.hp -= value
        super().damage(value)

A = Grenade(100)
C = Player(4000)
A.explode(C)
A.explode(C)