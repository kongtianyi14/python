"""
练习：
创建父类：车(品牌，速度)
创建子类：电动车(电池容量,充电功率)
创建子类对象并画出内存图。
"""


class Car:
    def __init__(self, brand="", speed=0):
        self.brand = brand
        self.speed = speed


class EleCar(Car):
    def __init__(self, brand="", speed=0, battery=0, power=0):
        self.battery = battery
        self.power = power
        super().__init__(brand, speed)
