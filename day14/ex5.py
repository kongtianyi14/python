"""
    小明可以使用手机打电话，也可以使用座机...
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def phone_call(self,tool):
        print(self.name,"打电话")
        tool.using()

class Tool:
    def using(self):
        pass

class Mobilephone(Tool):
    def using(self):
        pass

class Landline(Tool):
    def using(self):
        pass