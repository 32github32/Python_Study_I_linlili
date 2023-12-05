#终端输入pip install requests 安装出现successful
#我们输入的网址 www.bilibili.com   （浏览器自动加上http://）
#实际完整的URL  ：http://www.bilibili.com
#
import requests
head ={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; ×64)"}  #把爬虫程序 伪装成正常浏览器（类型，版本，电脑操作系统）
                                                                   #代码发送请求：User-Agent: python-requests/2.22.0
response = requests.get("http://books.toscrape.com/")
print(response)          #<Response [200]> 200=状态码 = status_code = 请求成功

#根据状态码，判断是否请求成功
if response.ok:
    print(response.text)
else:
    print("请求失败")