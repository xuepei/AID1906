"""
    变量语法与del
"""
#语法1： 名称=对象

#语法2：名称1，名称2=对象1，对象2

#语法3：名称1=名称2=对象

#启发：变量交换
#变量1，变量2=变量2，变量1

#------------------------
skill01="乾坤大挪移"
skill02=skill01
#删除变量
del skill01
skill02="九阳神功"

"""
    练习：
    dog01="米修"
    dog02="多度"
    dog01=dog02
    dog03=dog02
    del dog02,dog03
    
#多度还在(因为变量dog01在引用)

print(dog01)
#访问已经删除的变量，会引发错误
"""