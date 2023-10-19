"""
定义函数，根据年月日计算是这一年的第几天.
如果2月是闰年,则29天平年28

month = int(input("请输入月:"))
day = int(input("请输入日:"))
days_of_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
total_days = sum(days_of_month[:month - 1])
total_days += day
print(f"{month}月{day}日是第{total_days}天.")

year = int(input("请输入年份:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
day = 29
else:
day = 28
"""


def compute_year_eryue_day(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return 29
    return 28


def compute_total_day(y, m, d):
    days_of_month = (31, compute_year_eryue_day(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    total_days = sum(days_of_month[:m - 1])
    total_days += d
    # print(f"{y}年{m}月{d}日是第{total_days}天.")
    return total_days


y = int(input("请输入年:"))
m = int(input("请输入月:"))
d = int(input("请输入日:"))
result = compute_total_day(y, m, d)
print(f"{y}年{m}月{d}日是第{result}天.")
