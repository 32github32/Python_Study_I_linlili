#子类没有 ，调用父类  # 子类有 ，用子类自己的
#子类写super
# 动物 ：人  猫
class Employee:  #首先定义一下 员工这个父类
    def __init__(self,name,id):         # 共同属性 inti
        self.name = name
        self.id =id
    def print_info(self): #定义一个打印信息的方法
        print(f"员工名字{self.name}，工号：{self.id}")

class FulltimeEmployee(Employee):   #子类=全职员工 ， 继承于Employee
    def __init__(self,name,id,monthly_salary ):
        super().__init__(name,id)
        self.monthly_salary = monthly_salary   #全职员工的月薪属性

    def calculate_monthly_pay(self):      #计算 月工资
        return self.monthly_salary

class ParttimeEmployee(Employee):    #兼职员工
    def __init__(self,name,id,daily_salary,work_days):   #要把所有属性汇总起来
        super().__init__(name,id)            #继承了两个属性，又多加了两个属性
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary*self.work_days

wang = FulltimeEmployee("小王","1002","10000")
lee = ParttimeEmployee("小李","002",150,16)    #注意数字不能打引号 ，不然变为字符串就乘不了

wang.print_info()
lee.print_info()    #打印的是父类的信息
print(wang.calculate_monthly_pay())
print(lee.calculate_monthly_pay())


