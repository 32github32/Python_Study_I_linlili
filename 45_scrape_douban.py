import requests
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"
}     #任意网页 →右键 →检查→刷新 →network网络 →headers标头→ user_Agent
response = requests.get("http://movie.douban.com/top250",headers = headers)  #找到网站输入连接http://movie.douban.com/top250
print(response.status_code)
print(response.text)

#418= 不想理爬虫
#User-Agent: 不是下划线