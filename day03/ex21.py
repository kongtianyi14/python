"""
    录入5人成绩最后打印平均成绩
    录入多人成绩直到输入空字符，最后打印平均成绩。
"""
# total = 0
# for i in "12345":
#     total += int(input("请输入第"+i+"个人的成绩:"))
# print("平均成绩为"+str(total/5))


total = 0
count = 1
while True:
    A = input("请输入第" + str(count) + "个人的成绩:")
    if A == "":
        break
    else:
        count += 1
        total += int(A)
print(total / (count - 1))
