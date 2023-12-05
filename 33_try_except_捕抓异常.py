#异常类型
# IndexError 索引错误
# number_list = [15,16,18,19,41]
# number_list = [4]    用索引之外的索引
#
# ZeroDivisionError 除零错误
# print(18/0)
#
# FileNotFoundError 找不到文件错误
# f = open("./hi.txt","r")    非write 打开的文件不存在
#
# TypeError 类型错误
# "yoo" *"hi"    两个字符串做乘法
#
# IndentationError 缩进错误
# ImportError 导入模板错误
# ArithmeticError 计算错误
# SyntaxError 语法错误
# AttributeError 属性错误
# ValueError 值错误
# KeyError 键错误

try:
    user_weight = float(input("请输入您的体重(单位：kg)："))   #放上你觉得可能报错的代码
    user_height = float(input("请输入您的身高（单位：m)："))    #用户输入 中文十八
    user_BMI = user_weight / user_height **2
except ValueError:   #except + 可能发生的错误类型
    print("告知用户输入了不合理的数字，提前吐槽")
except ZeroDivisionError:
    print("用户把身高输入为  0，请输入正确身高")
except:
    print("不知道会发生什么错误，有错就给这个提示.前面的except捕抓到，就不会被执行")

else:
    print("用户输入没问题 ，打印BMI值为:"+str(user_BMI))
finally:
    print("无论错误发生与否，都会被执行的语句：程序结束运行")

#assert 断言 + 后面加布尔函数

assert len("Hi") == 2  #无事发生

assert 1+2<6  #AssertError 断言错误

assert "a"in ["b","c"]