"""
    标准属性
    @property
    @名字.setter
"""
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.set_age(age)
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 80:
            value = 80
        elif value < 20:
            value = 20
        self.__age = value


    # age = property(get_age,set_age)

a_ke = Wife("阿珂",100)
print(a_ke.age)