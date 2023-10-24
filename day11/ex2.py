"""
    小明请保洁打扫卫生
"""


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def notify(self):
#         print("发出通知")
#         cleaner = Cleaner()
#         cleaner.cleaning()
#
# class Cleaner:
#     def cleaning(self):
#         print("打扫卫生")
#
# xm = Person("小明")
# xm.notify()

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.cleaner = Cleaner()
#     def notify(self):
#         print("发出通知")
#         self.cleaner.cleaning()
#
# class Cleaner:
#     def cleaning(self):
#         print("打扫卫生")
#
# xm = Person("小明")
# xm.notify()

class Person:
    def __init__(self, name):
        self.name = name

    def notify(self,cleaner):
        print("发出通知")
        cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")


xm = Person("小明")
clean_robot = Cleaner()
xm.notify(clean_robot)
