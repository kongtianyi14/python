"""
    行
    物理行
    a = 1
    b = 2
    c = a + b
    逻辑行
    a = 1;b = 2;c = a + b;print(c)
"""
# 换行符号
d = 1+\
    2+\
    3+\
    4+\
    5+\
    6
print(d)

# --括号
e = (1 + 2 +
     3 + 4 +
     5 + 6)
print(e)
# 值得注意的是，对于python来说缩进是很重要的事情，否则会出现unexpected indent
#推荐使用快捷键在pycharm中 ctrl+alt+L