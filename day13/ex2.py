"""
以面向对象思想,描述下列情景.
张无忌教赵敏九阳神功
赵敏教张无忌玉女心经
张无忌工作挣了5000元
赵敏工作挣了10000元
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def teach_skill(self,target,skill):
        print(f"{self.name}教{target.name}{skill}")

    def work(self,money):
        print(f"{self.name}工作挣了{money}")

zwj = Person("张无忌")
zm =Person("赵敏")

zwj.teach_skill(zm,"九阳神功")
zm.teach_skill(zwj,"玉女心经")

zwj.work(5000)
zm.work(10000)