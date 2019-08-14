"""
    练习：
    是闰年的条件：
    (1)年份能被4整除，但不能被100整除
    (2)年份不能被400整除
"""
year=int(input("请输入一个年份："))
# if (year%4==0 and year%100!=0) or (year%400!=0):
#     print(True)
# else:
#     print(False)
result=(year%4==0 and year%100!=0) or (year%400!=0)
print(result)