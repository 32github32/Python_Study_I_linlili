#之前学的都是【面向过程】 要实现的事情拆分成一个个步骤
#面向过程 = 编年体
#面向对象 = 纪传体
#面向对象  ① 模拟真实世界 ② 先考虑对象有什么性质，能做什么事情  ③提出（属性）性质 定义ATM类 ④ 用类创建对象
# 类 vs 对象 ①类是创建对象的模板  ④对象是类的实例
# 类   + 对象（属性/性质）
# 方法 + 对象（行动步骤）
#
#面向对象 ：
# ①封装 ： 写类的人将内部细节隐藏起来
# ②继承：爷爷→爸爸→儿子  小学生 大学生 继承学习的类
# ③ 多态：小学生也大学生作业内容不一样
#
#C ：纯面向过程
#java： 纯面向对象
#
#类对象
class CuteCat:  # 类用pascal命名法 ：首字母大写分隔单词  m冒号表示下方还有东西
    def __init__(self,cat_name,cat_age,cat_color):   # 构造函数 定义实例对象的属性 必须被命名为 __init_   第一个参数永远是self被占用用于表示对象自身
        self.name = cat_name                       #   接来下是定义 类的代码
        self.age = cat_age
        self.color = cat_color
cat1 = CuteCat("jojo",2,"green")         #可爱猫猫的类
print(cat1.name)
#
#类方法
class CuteCat:
    def speak(self):
        print("喵"* self.age)

    def think(self,content):
        print("小猫{self.name}在思考{content}")

