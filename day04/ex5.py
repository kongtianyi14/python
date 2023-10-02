"""
在终端录入一个内容，循环打印每个字对应的ASCII值
"""
# message = input("请输入内容：")
# for item in message:
#     print(ord(item))
"""
循环录入编码值打印文字，直到输入空字符为止
"""
while True:
    number = input("请输入编码值：")
    if number == "":
        break
    else:
        character = chr(int(number))
        print(character)
