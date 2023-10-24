"""
创建敌人类，并保护数据在有效范围内
数据：姓名、攻击力、血量
            0-100   0-500
"""
class Enemy:
    def __init__(self, name="", damage=0, hp=0):
        self.name = name
        self.damage = damage
        self.hp = hp

    def get_hp(self):
        return self.__hp

    def get_damage(self):
        return self.__damage

    def set_damage(self,value):
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        self.__damage = value

    def set_hp(self,value):
        if value > 500:
            value = 500
        elif value < 0:
            value = 0
        self.__hp = value

    hp = property(get_hp, set_hp)
    damage = property(get_damage, set_damage)

mie_ba =Enemy("灭霸",800,1000)
print(mie_ba.damage)
print(mie_ba.hp)