# def func01(p1,p2):
#     p1 = 10
#     p2[0] = 20
#     return 30
# data01 = 1
# data02 = [2]
# data03 = func01(data01,data02)
# print(data01)
# print(data02)
# print(data03)

# def func01(p1, p2):
#     p1 = "孙悟空"
#     p2["八戒"] += 50
# a = "悟空"
# b = {"八戒": 100}
# func01(a, b)
# print(a)  # ?
# print(b)  # ?

# def func01(p1, p2):
#     p1 = 100
#     p2[0] = 200
# a = [10]
# b = [20]
# c = func01(a, b)
# print(a) # ?
# print(b) # ?

def func01(p1,p2):
    p1 = [100,200]
    p2[:1] = [300]

a = [10,20]
b = [30,40]
func01(a,b)
print(a)
print(b)