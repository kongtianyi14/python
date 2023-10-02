"""
    字符串：由一系列字符组成的不可变序列容器，存储的是字符的编码值。
    列表：由一系列变量组成的可变序列容器。
"""
# 1. 创建
# 写法1:列表名 = [数据1,数据2]
# 姓名列表
list_names = ["悟空", "唐三藏", "八戒", "沙僧"]
# 年龄列表
list_ages = [26, 23, 25, 16]
# 写法2:列表名 = list(可迭代对象)
list_name = list("孙悟空")
print(list_name) # ['孙', '悟', '空']
# 2. 添加
# -- 追加:列表名.append(数据)
list_names.append("小白龙")
# -- 插入: 列表名.insert(索引,数据)
list_names.insert(2, "哪吒")#他将占用列表中的第三个位置
print(list_names) # ['悟空', '唐三 藏', '哪吒', '八戒', '沙僧', '小白龙']
# 3. 定位
# -- 索引：容器名[整数]
# -- 读取
element = list_names[-1]
print(element) # 小白龙
# -- 修改
list_names[-1] = "二郎神"
print(list_names) # ['悟空', '唐三藏', '哪吒', '八戒', '沙僧', '二郎神']
# -- 切片:容器名[整数:整数:整数]
# -- 通过切片读取，创建新列表(拷贝)
names = list_names[:3]
print(names) # ['悟空', '唐三藏', '哪吒']
# -- 通过切片修改，遍历右侧数据,依次存入左侧.
list_names[:3] = ["空空", "唐唐", "猪猪"]
# list_names[:3] = 100 # 因为100不能被for
list_names[:3] = "孙悟空"
print(list_names) # ['孙', '悟', '空', '八戒', '沙僧', '二郎神']
# 4. 遍历:操作容器每个元素
# -- 方式1： for 元素 in 容器
# 适用性：从头到尾依次读取
for name in list_names:
    print(name)
# -- 方式2：for 索引 in range(开始,结束,间隔):
# 适用性：从头到尾依次修改
for i in range(len(list_names)):
# 文字长度是3的修改为None
    if len(list_names[i]) == 3:
        list_names[i] = None
print(list_names) # ['孙', '悟', '空', '八戒', '沙僧', None]
# 5. 删除
# -- 方式1：根据元素删除 列表名.remove(元素)
list_names.remove("八戒")
# -- 方式2：根据定位删除 del 容器名[索引或者切片]
del list_names[0]
del list_names[-2:]
print(list_names) # ['悟', '空']