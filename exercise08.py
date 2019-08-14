"""
    在控制台中获取匀变速直线运动的位移与时间公式：
    距离=初速度×时间+加速度×时间的平方×0.5
    已知：距离，时间，初速度
    计算：加速度
"""
distance=float(input("请输入距离："))
time=float(input("请输入时间："))
v=float(input("请输入初速度："))
a=(distance-v*time)*2/(time**2)
# distance =v*time+a**time*0.5
print("加速度为："+str(a))

"""
    在控制台中获取一个四位整数：1234
    计算每位相加和1+2+3+4
    提示：17-->17//10,17%10
"""