"""
闰年29天
平年28天
判断条件：年份能被4但是不能被100整除，或者年份能被400整
除，则为闰年。
"""
year = int(input("请输入年份:"))
if year % 4 == 0 and year % 100!= 0:
    print("闰年29天")
elif year % 400 == 0:
    print("闰年29天")
else:
    print("平年28天")


year = int(input("请输入年份:"))
day = 29 if not year % 4 and year % 100 or not year%400 else 28
print(day)