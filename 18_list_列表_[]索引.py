shopping_list= []                   #索引函数，列表函数 = 方括号。属于可变数据类型
shopping_list.append("keyboard")    #增补函数
shopping_list.append("mouse pad")
print(shopping_list)                           #键盘+鼠标垫
shopping_list.remove("keyboard")    #消减函数
print(shopping_list)                           # 鼠标垫
shopping_list.append("player")
shopping_list.append("chair")                  #鼠标垫、播放器、椅子
print(shopping_list[0])             #打印列表第一个
shopping_list[0]="displayer or monitor"     #替换列表第一个    显示器、播放器、椅子
print(shopping_list[0])
print(len(shopping_list))         #一共3个

price = [1080,100,1000]
max_price = max(price)
min_price = min(price)
sorted_price= sorted(price)    #从小到大排序
print(max_price)
print(sorted_price)

#双方括号 ： 列表里面索引
print([1,2,3,4,5,6,7,8,9][0])


# list 列表   set 集合 tuple元组  字典。
#x = [28,180,80,12000]  #x0 = 28
#data = range (3)   # 0\1\2

#列表切片 list 【start ：end ： step 3】 每隔三个取一个。取n-1

