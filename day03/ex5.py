"""
在终端中录入4个同学身高,打印最高的值.
算法：
提示
假设第一个就是最大值
使用假设的和第二个进行比较, 发现更大的就替换假设的
使用假设的和第三个进行比较, 发现更大的就替换假设的
使用假设的和第四个进行比较, 发现更大的就替换假设的
最后，假设的就是最大的.
效果：
请输入第1个同学身高:170
请输入第2个同学身高:160
请输入第3个同学身高:180请输入第4个同学身高:165
最高的同学:180
"""
a = int(input("请输入第1个同学身高:"))
b = int(input("请输入第2个同学身高:"))
c = int(input("请输入第3个同学身高:"))
d = int(input("请输入第4个同学身高:"))
max = a
if a <= b:
    max = b
if b <= c:
    max = c
if c <= d:
    max = d
print("最高身高为："+str(max))
# 这个例子相当重要，他是不光是对if语句的一个联系，也是首次系统地接触算法这个思维