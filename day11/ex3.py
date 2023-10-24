"""
以面向对象思想,描述下列情景.
玩家攻击敌人,敌人受伤(头顶爆字).
"""
class Player:
    def __init__(self, name):
        self.name = name

    def attack(self,whos):
        print("发起攻击")
        whos.damage()

class Enemy:
    def damage(self):
        print("头顶爆字")

kongtianyi = Enemy()
lurenjia = Player("lurenjia")
lurenjia.attack(kongtianyi)