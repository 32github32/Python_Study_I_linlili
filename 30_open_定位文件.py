#绝对路径：
# c:
# c:\home
# c:\home\data
# c:\home\data\a.py

#相对路径：我正在编辑的代码.py 相对的位置
# ../..
# ..
# .           #.表示当前文件所在的目录
# ./data
# ./data/a.py   = data/a.py    #  ./点斜杠可以省略

#open("E:\1.pycharm.file","r")  #r =read 读取模式（只读）不写默认读取r   #FileNotFoundError 程序找不到文件名
#open("E:\1.pycharm.file","r")  #w = write 写入模式（只写）
f = open("./data.txt","r",encoding="utf-8") #文件的一般编码方式是utf8  #txt好一点 office有子体字号颜色的设置
print(f.read())       #读完
#print(f.read(10))     #会读1-10个字节  #读完之后接下来都默认空值了
#print(f.read(10))     #11-20个字节
#print(f.readline())   #读一行

f.close()                 #关闭文件，释放资源