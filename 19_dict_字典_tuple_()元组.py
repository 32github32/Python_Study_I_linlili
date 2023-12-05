#元组和列表list很像
# example_tuple = ("键盘","键帽")   #元组是圆括号
# # example_tuple.append("显示器")  #元组不可变 ，不可用 append 加 remove 减 会报错
# # example_tuple.remove("显示器")
#
#
# example_list = ["键盘","键帽"]    #列表是方括号
# example_list.append("显示器")
# example_list.remove("显示器")

#字典contacts 里面有三个张伟。("张伟",23)这个元组作为一个键，找到里面那个23岁的张伟
contacts={("张伟",23):"15000000000",("张伟",34):"15000000001",("张伟",56):"15000000002"}
zhangwei23_phone =contacts[("张伟",23)]
print(zhangwei23_phone)              #15000000000

#覆盖
contacts[("张伟",34)]="15011111111"   #{('张伟', 23): '15000000000', ('张伟', 34): '15011111111', ('张伟', 56): '15000000002'}
print(contacts)

#添加
contacts[("张伟",78)]="15000000003" #{('张伟', 23): '15000000000', ('张伟', 34): '15011111111', ('张伟', 56): '15000000002', ('张伟', 78): '15000000003'}
print(contacts)
contacts["小明"]="18500000009"
print(contacts)

#想知道是否存在张伟56
print(("张伟",56) in contacts)   #True

#删除键值对
del contacts["小明"]
print(contacts)

#想知道字典有多少键值对
print(len(contacts))


slang_dict = {"sleep":"shui_jiao","yyds":"shen","jian":"zhi"}              #{} = total
#① 花括号 = 字典  ② 引号=字符串  ③ 冒号 键：值  ④ 逗号 下一个
#del删除键
#temperature_dict.keys():    返回里面的所有键
#temperature_dict.values():   返回里面的所有值
#temperature_dict.items():    键值对    变量_couple  变量被赋值为键+值组成的元组

slang_dict["study"]="happy life"                                           #add to dictionary  方括号[]= append
#{"sleep":"shui_jiao","yyds":"shen","jian":"zhi","study":"happy life"}
#键:值
#,逗号表示下一对

query = input("pleasse enter the slang you want to query:")
if query in slang_dict:                                                    # whether the query item is in the dictionary
    print("the meaning of your query of "+ query + " is as follow")
    print(slang_dict[query])
else:
    print("the slang you inquired are not included")
    print("The current number of entries in this dictionary is:" + str(len(slang_dict))) #str = "" output string