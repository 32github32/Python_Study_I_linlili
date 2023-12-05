contacts = ["老1","老2","老3","老4","老5","老6","老7","老8","老9","老0"]  #[] 直接表示_list_了？
for name in contacts:
    message_content = name + "您好！祝福" + name + "新年快乐!"
    print(message_content)
# send message (name, message_content)  根据名字发给相应的联系人
year = "虎"
for name in contacts:
    message_content = """
    hhhh
    llll
    aaaa
    祝福{1}
    {0}年大吉
    """.format(year,name)
    print(message_content)
#注意format 的格式
gpa_dict = {"刘二":3.111,"张三":3.2222,"李四":3.3333,"王五":3.44444}
for name,gpa in gpa_dict.items():
    message_gpa = "{0}同学你好，你的绩点为：{1:.2f}".format(name,gpa)  # ① 不要+号 ② :.2f 保留两个浮点数
    print(message_gpa)

#简写 （f"  ",）

#老师讲了一下