"""
    封装 行为角度
    私有成员：
-- 作用：无需向类外提供的成员，可以通过私有化进行屏蔽。
-- 做法：命名使用双下划线开头。
-- 本质：障眼法，实际也可以访问。
私有成员的名称被修改为：类名__成员名，可以通过__dict__属性查看。
"""
class MyClass:
    def __init__(self, data):
        self.__data = data

    def __func01(self):
        print("func01执行了")
    #公开成员可以对内部进行访问
    def func02(self):
        self.__data
        self.__func01()
m01 = MyClass(10)
# print(m01.__data) # 无法访问
print(m01._MyClass__data)
print(m01.__dict__) # {'_MyClass__data': 10}
# m01.__func01() # 无法访问
m01._MyClass__func01()
m01.func02()#公开成员可以对内部进行访问  