# BMI = weight/height**2

#身高。体征 = 浮点数（input 函数）
#please enter your weight(units:kg):
#重要的是 用户输入的值 再去float
# input 是连接运算
user_weight = float(input("please enter your weight(units:kg):"))
user_height = float(input("please enter your height(units:m):"))

#被定义
user_BMI = user_weight/(user_height**2)

#打印（字符串 + 字符串）     字符串不能喝int/float连在一起，不然就是四不像
print("Your BMI is:"+str(user_BMI))    # + 不是字符串 ，放心用


print(2+2)             #4
print(0.2+0.2)         #0.4

