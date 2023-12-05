# BMI = weight/height**2
user_weight = float(input("please enter your weight(units:kg):"))
user_height = float(input("please enter your height(units:m):"))
user_BMI = user_weight/(user_height**2)
print("Your BMI is:"+str(user_BMI))

#偏瘦:<=18.5
#正常:18.5~25
#偏胖:25~30
#肥胖:>=30           等于号 = =  ！！！

if user_BMI<=18.5:
    print("the BMI value belongs to the lean range")
elif 18.5 < user_BMI <= 25:              #equivalent to an interval
    print("BMI is in the normal range")
elif 25 < user_BMI <= 30:
    print("BMI falls into the overweight range")
else:                                    # you don't have to type anymore
    print("BMI falls into the obese range")

#嵌套条件语句 ： 条件语句if/else 里面在放入条件语句elif
#相当于一个区间
#elif没有数量限制

#三种逻辑结构

#顺序结构 ：一条路。list
#选择结构 ：左边右边。  else
#循环结构：