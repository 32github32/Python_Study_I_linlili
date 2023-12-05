class Student:
    def __init__(self,name,student_id):  #构造函数+参数    #以下是一个一个构造
        self.name = name
        self.student_id = student_id
        self.grades = {"语文":0,"数学":0,"英语":0}   #定义一个字典，

    def set_grade(self,course,grade):   #制定成绩 = 定义函数       #以下是被定义的内容  #这里的course grade 不加self
        if course in self.grades:       #self.grades = 上面的字典
            self.grades[course] = grade   #course没说明白？     该课程对应该成绩？
    def print_grades(self):
        print(f"学生{self.name}(学号:{self.student_id})的成绩为:")    #format的方法
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")
chen = Student("小陈","1001")
wang = Student("小王","1002")

print(chen.name,chen.student_id)    #chen 的 名字、 chen的学号。
wang.set_grade("数学",95)
wang.set_grade("语文",98)
wang.set_grade("英语",100)
print(wang.grades)