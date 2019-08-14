"""
    bool
    比较运算符
    逻辑运算符
"""
#1.bool           int        类型
#True False      10,20,30...  数据
#命题：带有判断性质的陈述句。
#      我是个男人   对的(True)
#      我是个坏人   错的/假的(False)
#      1>2        错的/假的(False)

#2.比较运算符 < > <= >= == !=
# 结果=变量1 > 变量2

print(1>2)#False

#3.逻辑运算符 与 或 非
#   判断两个命题(bool值)关系
#    总结：一假俱假  表达的是"并且"的关系(必须都满足)
result = True and True
result = True and False
result = False and True
result = False and False
print(result)

#总结：一真俱真  表达的是"或者"的关系(满足一个就可以)
result = True or True
result = True or False
result = False or True
result = False or False
print(result)

#非
result = not True
result = not False
print(result)

"""
    练习：
    是闰年的条件：
    (1)年份能被4整除，但不能被100整除
    (2)年份不能被400整除
"""











