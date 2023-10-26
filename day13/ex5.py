"""
练习：
创建子类：狗(跑)，鸟类(飞)
创建父类：动物(吃)
体会子类复用父类方法
体会 isinstance 、issubclass 与 type 的作用
"""
class Animal:
    def eat(self):
        print("吃")

class Dog(Animal):
    def run(self):
        print("跑")

class Bird(Animal):
    def fly(self):
        print("飞")

A = Animal()

D = Dog()
D.eat()
D.run()

B =Bird()

#类型 类型
print(issubclass(Animal,Dog))

#对象 类型
print(isinstance(B,Animal))

#对象 类型
print(type(D) == Animal)