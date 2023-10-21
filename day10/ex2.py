"""
    面向过程
        自己干
    面向对象
        找人干
            类
                数据：品牌、价格、颜色..
                行为：通话..
        具体流程：
            现实世界            虚拟世界

        class 类名:
            def __init__(self,参数):
                self.实例变量 = 参数
            def 实例方法(self,参数):
                pass
"""


class Wife:


    def __init__(self, name, age, sex):
        # 初始化对象数据
        self.name = name
        self.age = age
        self.sex = sex

    # 行为(方法=函数)


    def play(self):
        print(self.name, "玩耍")


# 调用构造函数(__init__)
shang_er = Wife("双儿", 26, "女")
# 操作对象的数据
shang_er.age += 1
print(shang_er.age)
# 调用对象的函数
shang_er.play()  # 通过对象地址调用方法,会自动传递对象地址.
# play(shanger)
print(shang_er)  # <__main__.Wife object at 0x7f390e010f28>
