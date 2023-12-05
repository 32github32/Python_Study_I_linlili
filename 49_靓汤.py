#终端输入：pip install bs4
#Beautiful soup 靓汤：① python中可以用来做html解析的库  ②和Requests是第三方库

from bs4 import BeautifulSoup  #从BS4库里面引入BeautifulSoup
import requests
content = requests.get("http://books.toscrape.com/").text   #发送get请求，请求获得 网站text内容，字符串形式储存到content这个变量里
soup = BeautifulSoup(content,"html.parser")  #将网站内容传入到 BS4的构造函数里，让BS去解析
                   #解析内容content  和制定解析器parser

#通透浏览器的检查功能 ，查看价格发生每个学习都在p元素里

all_prices = soup.findAll("p",attrs={"class":"price_color"})
                     #attrs = 可选参数
for prices in all_prices:
    print(prices.string[2:])  # 索引值大于等于2的所有剩下的字符串（.≠，）
                          #string属性会把标签包围的文字返回来给我们


from bs4 import BeautifulSoup                                 #bs4库里面引入靓汤
import requests                                               # 引出其它库的请求
content = requests.get("http://books.toscrape.com/").text     #内容 = 请求获得网站的文本内容
soup = BeautifulSoup(content,"html.parser")                   #汤 = 靓汤解析，该内容 ，用parser的方法
all_titles = soup.findAll("h3")                               #所有的标题 = 汤的功能找h3
for title in all_titles:                                      #for循环 所有标题
    all_links = title.findAll("a")                            #找连接
    for link in all_links:                                    #
        print(link.string)                                    #打印 文字内容
