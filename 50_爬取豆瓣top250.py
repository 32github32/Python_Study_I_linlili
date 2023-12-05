import requests                             #引入网站请求，可以进入网站
from bs4 import BeautifulSoup               #引入靓汤，可以解析网站
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"
}                                           #请求头：表明是浏览器
for start_num in range(0,250,25):           #结束值不包含在输出范围,第三个值25 = 数值每次增加多少

    response = requests.get(f"http://movie.douban.com/top250?start={start_num}",headers = headers)
                                                #响应内容：请求获取该网站信息
    html = response.text                        #响应后 得到的文本
    Soup=BeautifulSoup(html,"html.parser")      #BS(解析内容，解析器) = 获得解析 = 文本 = 汤
    all_titles  = Soup.findAll("span",attrs={"class":"title"})
    #findall的方法（第一个参数span传入标签名，attrs = 根据原始的属性来提取，我们希望这个元素的class属性，他的值是title）
    #class属性为title的span元素
    #findall返回的是一个可迭代的对象，用for循环迭代 可迭代的对象
    for title in all_titles:
        title_string = title.string   #title的string属性，span标签就没有了      ②变量_ = 某个属性.
        #出现原版标题，原版标题前面都有一个斜杠，找到不带斜杠的
        if"/" not in title_string:
            print(title_string)
            #但是只能拿到第一页 前25的电影  https://movie.douban.com/top250
            #点击第二页，看到它的链接       https://movie.douban.com/top250?start=25&filter=
            #start = 25 从第二页开始，电影索引从25开始，生活中就是从26开始
            #设置一个变量 start_num 开始数值0 25 50 75 ...   250   用for循环结合range  写在上面

            #print（start_num）发现无误 ，更新链接 "http://movie.douban.com/top250"
            #改为                              f"http://movie.douban.com/top250?start={start_num}"
