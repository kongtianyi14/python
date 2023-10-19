"""
求列表最小值
"""


def find_min_list(list_name):
    min = list_name[0]
    for i in range(1, len(list_name)):
        if list_name[i] < min:
            min = list_name[i]
    return min

# def A(B):
#     pass