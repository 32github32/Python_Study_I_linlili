# 扇形面积 = θ/360°*（π*r**2）     θ = 圆心角
central_angle_1 = 160
radius_1 = 30
sector_area_1 = central_angle_1/360*(3.14*radius_1**2)
print(f"此扇形的面积为：{sector_area_1}")   # print(f"    ")   是format函数

# Dry 原则 ：don't repeat youself          #def 开始定义函数 + 被定义的函数（）：   定义为9 10  的内容
def calculate_sector(central_angle,radius):     #给圆心角  半径  两个参数
    sector_area = central_angle / 360 * (3.14 * radius ** 2)        #被定义的内容
    print(f"此扇形的面积为：{sector_area}")              #定义函数 9 10  不会被执行     只有调用的时候才会被执行

calculate_sector(160,30)
calculate_sector(170,60)