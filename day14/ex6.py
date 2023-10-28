"""
    玩家可以攻击敌人，敌人受伤（头顶爆字，血量减少），还有可能死亡（加分）、
    敌人可以攻击玩家，玩家受伤（碎屏，血量减少），还有可能死亡（充值）
"""


class Game:
    def attack(self, target_1, target_2):
        target_2.get_damage(target_1.attack)

class Person:
    def __init__(self, attack=0, hp=0):
        self.attack = attack
        self.hp = hp

    def get_damage(self, value):
        if self.hp > value:
            return True
        else:
            return False

#----------------------------------------------------------------------

class Player(Person):
    def __init__(self, attack=0, hp=0):
        super().__init__(attack, hp)

    def get_damage(self, value):
        print("碎屏")
        if super().get_damage(value):
            self.hp -= value
            print(self.hp)
        else:
            print("死亡，请充值")

class Enemy(Person):
    def __init__(self, attack=0, hp=0):
        super().__init__(attack, hp)

    def get_damage(self, value):
        print("头顶爆字")
        if super().get_damage(value):
            self.hp -= value
            print(self.hp)
        else:
            print("死亡，玩家+1分")

# ----------------------------------------------------------------------
A = Game()
test01 = Player(20,100)
test02 = Enemy(5,100)
A.attack(test01,test02)
A.attack(test01,test02)
A.attack(test01,test02)
A.attack(test01,test02)
A.attack(test01,test02)
A.attack(test01,test02)
