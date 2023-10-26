"""
创建技能类
技能名称、冷却时间 0 - 120、攻击力0 - 200、消耗法力(只读) 100 - 100
"""


class Skill:
    def __init__(self, name="", cd=0, damage=0):
        self.name = name
        self.cd = cd
        self.damage = damage
        self.__magic = 100

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, value):
        if value > 120:
            value = 120
        if value < 0:
            value = 0
        self.__cd = value
    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        if value > 200:
            value = 120
        if value < 0:
            value = 0
        self.__damage = value
    @property
    def magic(self):
        return self.__magic