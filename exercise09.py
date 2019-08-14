"""
    在控制台中获取一个四位整数：1234
    计算每位相加和1+2+3+4
    提示：17-->17//10,17%10
"""

number=int(input("请输入一个四位整数："))
entries=number%10
shiwei=number//10%10
baiwei=number//100%10
qianwei=number//1000
total=entries+shiwei+baiwei+qianwei

print("每位相加之和为：",str(total))