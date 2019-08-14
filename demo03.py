"""
    名称=对象
    核心数据类型
        变量没有类型，关联的对象才有类型。
"""
#None 空
#占位；只希望有个变量，指向的对象还不确定。
name=None

skill01="乾坤大挪移"
#解除乾坤大挪移与变量skill01关系
skill01=None

#2.整形(整数)
number01=240
#十进制、二进制0b、八进制0o、十六进制0x
#浮点型(小数)
#a=10.5 = 1.05e

#4.字符串
message01="peixue"
t=type(message01)
print(t)
#5.复数
number=10+10.5j
print(type(number))

#6.类型转换
#input函数的结果是字符串类型
age=input("请输入年龄：")
#str-->int
int_age=int(age)
#int-->str
print("明年是："+str(int_age))






