"""
    在控制台中获取一个变量
    再在控制台中获取一个变量
    交换这两个变量
    最后输出这两个变量

    变量名称=input("提示的信息：")
    print(变量名)
"""

number01=input("请输入一个变量：")
number02=input("请输入第二个变量：")

temp=number01
number01=number02
number02=temp

print(number01,number02)


