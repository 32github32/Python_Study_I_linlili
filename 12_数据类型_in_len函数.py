#第一大类：不可变数据类型
#字符串str
print("hello")
print("呦")             #①文本内容，被引号包裹，无逻辑意义，作为字符而存在

print(len("hello"))    #② 空格 数字 符号 都是一个长度
print(len(" hello"))
print(len("1hello"))
print(len("？hello"))

print(len("he\nllo"))   #\n  = 一个字符

print("hello"[1])       #[]索引  提取第一个字符= 现实中的第二个

#整数  int("666") = 六百六十六
print(int("666")-600)

#浮点数  float（"666.6"）
print(float("666.6")-0.6)

#布尔类型bool      【必须大写】  （怎么用？）：True  False
#想知道是否存在张伟56
contacts={("张伟",23):"15000000000",("张伟",34):"15000000001",("张伟",56):"15000000002"}
print(("张伟",56) in contacts)   #True
print(len(contacts))

#空值类型 NoneType 【必须大写】 = None

#元组=键key （不可变 ，但很像列表）
example_tuple = ("键盘","键帽")   #元组是圆括号
# example_tuple.append("显示器")  #元组不可变 ，不可用 append 加 remove 减 会报错
# example_tuple.remove("显示器")




example_list = ["键盘","键帽"]    #列表是方括号   （，），[，]符号才是代表
example_list.append("显示器")
example_list.remove("显示器")


#第二大类：可变数据类型（通过函数去定义怎么变）
#列表

#字典：键值对 keys value

#第三大类：不确定数据类型   先找  因为：数据类型能决定你用哪些函数
print(type("Hello!"))    #得出<class 'str'> 字符串类
print(type(6))           #<class 'int'>
print(type(6.0))         #<class 'float'>



