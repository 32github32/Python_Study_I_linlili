# 网站服务区
# 客户端 = 浏览器：渲染 解析网页内容 储存或分析数据
# DDoS攻击 通过给服务器发送海量的高频请求
# 优秀网站要登录 ， 验证码 不要强行突破
# robot.txt 会告诉你那些网页可以爬取

# HTTP请求  hypertext transfer protocol  超文本传输协议
# GET方法：获得数据 = 【主要】
# POST方法：创建数据（提交账号注册表单）

#请求行：POST/user/info HTTP/1.1
#      POST/user/info？new_user=true HTTP/1.1
#       POST（方法类型）/user/info（资源路径） HTTP/1.1（协议版本
#       www.douban.com/movie/top250（资源路径）?start=75&filter=unwatched（？后面=查询参数：可以传递服务器额外的信息，不同信息用&间隔）
#                                             start=75 （返回用户的内容 从排在75的电影开始）
#                     /第一个斜杠 表示资料路径的跟
#
#请求头：包含一下给服务器的信息
# Host: www.example.com
#       主机域名
#             +请求头的user/info？new_user=true  = 完整的网站 ：www.example.com（域名）/user/info（路径）？new_user = true（查询参数）
# User-Agent: curl/7.77.0
#       告知服务器客户端的相关信息
# Accept:*/*
#       告诉服务器：客户端想想接收的响应数据是什么类型的 ，接收多种类型用逗号进行分隔 ， */*=啥类型都可以

#请求体：放客户端传给服务器的其它任意数据    get方法的请求体一般为空
#{"username"："林粒粒呀"，
#"email":"linliliya@hotmail.com"}



#http响应

# 状态行
# HTTP/1.1 200 OK
# HTTP/1.1（协议版本） 200（状态码） OK（状态消息）
#
#          200 OK                      //客户端请求成功
#          301 Moved Permanently       //资源被永久移动到新地址
#          400 Bad Request             //客户端不能被服务器所理解
#          401 Unauthorized            //请求未经授权
#          403 Forbidden               //服务器拒绝提供服务
#          404 Not Found               //请求资源不存在
#          500 Internal Server Error   //服务器发生不可预期的错误
#          503 Server Unavailable      //服务器当前不能处理客户端的请求
#

#
# 响应头
# Date: Fri, 27 Jan 2023 02:10:48 GMT          日期和时间
# Content-Type: text/html; charset=utf-8       返回内容的类型text/html或者application/json，及编码格式utf-8
#
# 响应体 ： 服务器给客户端的数据内容
# <!DOCTYPE html>
# <head><title>首页</title></head>
# <body><h1>林粒粒呀</h1><p>哈喽！</p></body>
# </html>





