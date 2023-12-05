#列表 list1 = [1,2,3,4,5,6]
#字典 dict1 = {"Smith":1.78,"mary":1.58}   迭代（替换）:键 or 值
#字符串 str1 = "hello world"
#for 变量名 in 可迭代的对象:      #for循环
temperature_list = [36.4,36.6,36.8,37.0,37.2]
for temperature in temperature_list:
    if temperature >=37:                     #相当于给temperature赋值,temperature开始有意义
        print(str(temperature) + "terrible")
# but I don't know who


#找值 ， 找键  ，找键值对？
# temperature_dict.keys():    #返回里面的所有键
# temperature_dict.values():   #返回里面的所有值
# temperature_dict.items():    #所以键值对    变量_couple  变量被赋值为键+值组成的元组

temperature_dict = {"001":36.4,"002":36.6,"003":36.8,"004":37,"005":37.2}
for staff_id,temperature in temperature_dict.items():   #staff_id,temperature = key,value
    if temperature >=37:
        print(staff_id)

#想要直观一点
temperature_dict = {"001":36.4,"002":36.6,"003":36.8,"004":37,"005":37.2}
for temperature_tuple in temperature_dict.items():
    staff_id = temperature_tuple[0]       #有键有值就是tuple
    temperature = temperature_tuple[1]    #方括号 ，不是圆括号  ，大括号退一步为中括号
    if temperature >=37:
        print(staff_id)                #[0]字典第一个数  [2]字典第二个数

# range(5,10)      #整数数列（起始值，结束值），但不包括10.
# range(5,10,2)   #每次跨两个数字 5，7，9
total = 0
for i in range(1,101):
    total = total + i
    print(total)