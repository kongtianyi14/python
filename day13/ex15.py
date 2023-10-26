class Car:
    def __init__(self, brand="", speed=0):
        self.brand = brand
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > 120:
            value = 120
        elif value < 0:
            value = 0
        self.__speed = value

    def __str__(self):
        return f"{self.brand} 车速:{self.speed}"

class EleCar(Car):
    def __init__(self, brand="", speed=0, battery=0, power=0):
        super().__init__(brand, speed)
        self.battery = battery
        self.power = power

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        if value > 220:
            value = 220
        elif value < 180:
            value = 180
        self.__power = value

    def __str__(self):
        return super().__str__()

test01 = Car("benz",180)
print(test01)
test02 = EleCar("RR",110,200,270)
print(test02)

#爸爸的定义 儿子能用 反之不能