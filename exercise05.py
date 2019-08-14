"""
    练习1：在控制台中录入一个半径
        输出圆形的面积(公式：3.14*半径平方)
        格式：圆形的面积是：XXX
"""
# r=input("请输入圆的半径:")
# mianji=3.14*(int(r)**2)
# print("圆形的面积是："+str(mianji)+"。" )

"""
    练习2：在控制台录入一个商品单价。
    再录入一个购买的数量
    最后录入一个金额，计算应找回多少钱。
    
"""
shangpin=float(input("请输入商品的价格："))

number=int(input("请输入购买该商品的数量:"))

money=int(input("顾客实际给的金额："))

total=money-shangpin*number
print("实际应找回顾客的钱数为："+str(total)+"。")

