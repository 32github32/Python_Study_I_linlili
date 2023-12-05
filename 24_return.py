def calculate_BMI(weight,height):       #定义函数（变量）     下面是函数内容
    BMI = weight/height**2
    if BMI <=18.5:
        category = "thin"
    elif 18.5<BMI<=25:
        category = "normal"
    elif BMI<=30:
        category = "fat"
    else:
        category = "obese"
    print(f" 你的BMI分类为：{category}")
    return BMI                             #返回为公式 ：weight/height**2

calculate_BMI(65,1.70)
calculate_BMI(62,1.67)               #执行定义里面 ：print(f" 你的BMI分类为：{category}") ，而不是给结果
print(calculate_BMI(62,1.69))
