# write : 如果文件不存在 程序就会自动创建      如果文件存在 就会被清空
with open("./write.txt.","w",encoding="utf-8") as f:    #open as(作为) f  r改为w
    f.write("第一行")         #之前的东西被清空了！
    f.write("第二行，不会帮你自动换行，手动加换行符\n")
    f.write("第三行，被换行了。")

#a = add 附加 不会被清空    #文件不存在 帮你创建
with open("./write.txt.","a",encoding="utf-8") as f:
    f.write("hhhhhwwww")    #还是write


#r+   同时支持读写
# with open("./write.txt.","r+ ",encoding="utf-8") as f:
#     print(f.read())
#     f.write("last")        #追加 个last

