"""
排序函数
"""
#shift+F6 改名 变量名 文件名


def func_listsort(list_name):
    for r in range(len(list_name) - 1):
        for i in range(r + 1, len(list_name)):
           if list_name[r] < list_name[i]:
               list_name[r],list_name[i] = list_name[i],list_name[r]
    # return list_name

list01 = [5,15,25,35,1,2]
func_listsort(list01)
print(list01)