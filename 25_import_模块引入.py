#案例1
import statistics        #import + 模块名字   #引入 数学统计函数 statistics
print(statistics.median([15,7,8,36,54,9,5,8,5,4,2,3,5,88,9,55,2]))   #计算中位数
print(statistics.mean([15,7,8,36,54,9,5,8,5,4,2,3,5,88,9,55,2]))    #平均数

#案例2
from statistics import median                 #查看函数名源代码 ： 按住ctr 点击 该函数名
print(median([15,7,8,36,54,9,5,8,5,4,2,3,5,88,9,55,2]))

#案例3
from statistics import *       #statistics 模块所有内容都引入   不推荐  容易产生冲突
print(median([15,7,8,36,54,9,5,8,5,4,2,3,5,88,9,55,2]))   #计算中位数
print(mean([15,7,8,36,54,9,5,8,5,4,2,3,5,88,9,55,2]))

#案列4 ： 第三方模块 pypi.org 下载
#先用 terminal 终端安装 pip install akshare
#import akshare