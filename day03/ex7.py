"""
在终端中输入月份，打印相应的天数.
1 3 5 7 8 10 12 有 31天
2 有 29天
4 6 9 11 有 30天
超过月份提示月份有误
效果：
请输入月份:10
31天
"""
month = int(input("请输入月份:"))
# if month > 12:
#     print("您输入的月份有误！")
# elif month == 1:
#     print(str(month) + "月有31天")
# elif month == 3:
#     print(str(month) + "月有31天")
# elif month == 5:
#     print(str(month) + "月有31天")
# elif month == 7:
#     print(str(month) + "月有31天")
# elif month == 8:
#     print(str(month) + "月有31天")
# elif month == 10:
#     print(str(month) + "月有31天")
# elif month == 12:
#     print(str(month) + "月有31天")
# elif month == 4:
#     print(str(month) + "月有31天")
# elif month == 6:
#     print(str(month) + "月有31天")
# elif month == 9:
#     print(str(month) + "月有31天")
# elif month == 11:
#     print(str(month) + "月有31天")
# else:
#     print(str(month) + "月有29天")
if 1 <= month <= 12:
    if month == 2:
        print(str(month) + "月有29天")
    elif month == 4 or month ==6 or month ==9 or month ==11:
        print(str(month) + "月有30天")
    else:
        print(str(month) + "月有31天")
else:
    print("您输入的月份有误！")
