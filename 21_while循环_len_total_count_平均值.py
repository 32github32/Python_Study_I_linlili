#while 条件A
#    行动B          #如果A条件为真就会执行行动B，相比于for循环的次数，while的条件有区别
list1 = ["你","好","吗？","兄","弟！"]
for char in list1:
    print(char)
for i in range(len(list1)):  # len(list1)=一个值 #len返回项目数=5 #起始值=0 #i依次赋值为 0 1 2 3 4
    print(list1[i])    #list1[0] 、 list1[1] 、 、
#for 明确次数  while不明确次数
i=0
while i < len(list1): #第一次 i=0 0<5 执行print
    print(list1[i])
    i=i+1             #注意些递增，不然进入无限循环

print("我是一个求平均值的程序。")
total = 0
count = 0
user_input = input("请输入数字（完成所有数字输入后，请输入q终止程序）：")
while user_input != "q":
    num = float(user_input)
    total = total +num  #或者写为： total+=num
    count = count+1     #或者写为： count+=1
    user_input = input("请输入数字（完成所有数字输入后，请输入q终止程序）：")
if count == 0:   #o/o 在数学里面是不被允许的
    result == 0
else:
    result = total/count #不会被 while 执行
print("你输入的数字平均值为"+str(result))

