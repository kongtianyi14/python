"""
    玩家攻击，敌人受伤。
    血量根据攻击减少
    属性快捷键: props

    属性的只写操作
    age = property()
    @age.setter
    def age(self,value):
"""
# class Player:
#     def __init__(self, damage=0, hp=0):
#         self.damage = damage
#         self.hp = hp
#
#     @property
#     def damge(self):
#         return self.__damage
#
#     @damge.setter
#     def damage(self, value):
#         if value > 500:
#             value = 500
#         elif value < 0:
#             value = 0
#         self.__damage = value
#
#     @property
#     def hp(self):
#         return self.__hp
#
#     @hp.setter
#     def hp(self, value):
#         if value > 100:
#             value = 100
#         elif value < 0:
#             value = 0
#         self.__hp = value
#
#     def attack(self,Enemy):
#         print("发起进攻")
#         Enemy.damage
#
#
# class Enemy:
#     def damage(self):
#         print("收到伤害")
#

class Player:
    def __init__(self, damage=0):
        self.damage = damage

    def attack(self,Enemy):
        print("发起进攻")
        Enemy.damage(self)
class Enemy:
    def __init__(self,hp):
        self.hp = hp
    def damage(self,Player):
        print("收到伤害")
        self.hp -= Player.damage


A = Player(20)
B = Enemy(100)
A.attack(B)
print(B.hp)
A.attack(B)
print(B.hp)