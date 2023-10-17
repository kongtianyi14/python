"""
    FOR-FOR
"""
# for r in range(2):
#     for c in range(5):
#         print("*",end = "")
#     print()
"""
    打印
    *
    **
    ***
    ****
"""
# for r in range(4):
#     for c in range(r+1):
#         print("*", end="")
#     print()
"""
    FOR-FOR和二位列表的配合
"""
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
for r in range(len(list01)):
    for l in range(len(list01[0])):
        print(list01[r][l],end = "\t")
    print()
