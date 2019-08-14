"""
    古代的称一斤十六两 33/16
    在控制台中获取两， 计算是几斤零几两
"""
unit=float(input("给出需要换算的计两："))
unit01=unit//16
unit02=unit%16
print("换算结果为："+str(unit01)+"斤零"+str(unit02)+"两")
# a = 10000
# b = 20000
# c = a = b
# print(c,a,b)
# del a, b
#
# c = None
# print(c)