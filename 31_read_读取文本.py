
with open("./data.txt","r",encoding="utf-8") as f:    #open as(作为) f
    print(f.readline())   #读第一行
    print(f.readline())   #读第二行
#    print(f.readlines())

#    line = f.readline()    #读第一行
#    while line = ""        #判断当前是否为空
#        print(line)        #不为空则打印当前行
#        line = f.readline()#读取下一行 ， 否则退出循环
#
# #readlines方法
    lines = f.readlines()     #把每行内容储存到列表里   #缩进！！！
    for line in lines:        #遍历每行内容
        print(line)           #打印当前行             #缩进！！！






