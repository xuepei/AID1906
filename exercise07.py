"""
    在控制台中获取一个分钟数，
    再获取一个小时数，
    最后获取一个天数
    计算总秒数
    按照格式输出：总秒数是：XXX
"""
minute=int(input("请输入分钟数："))
hour=int(input("请输入小时数："))
day=int(input("请输入天数："))
time=minute*60+hour*60*60+day*24*60*60
print("总秒数是："+str(time))

"""
    在控制台中获取匀变速直线运动的位移与时间公式：
    距离=初速度×时间+加速度×时间的平方×0.5
    已知：距离，时间，初速度
    计算：加速度
"""