#函数名：my_calculate.py
def my_adder(x,y)
    return x+y


import.unittest                                          #Python 单元测试库：对软件中最小可测试单元进行验证
from 34_assert.py import my_adder                        #from (函数名) import （类名）

class TsetMyAdder(unittest.Testcase):                    #unittest库 Testcase 类 找test开头的子类进行测试
    def test_positive_with_positive(self):               #定义 测试用例 必须test_开头
        self.assertEqual(my_adder(5,3)8)                 #assertEqual（A,B）    assert断言A=B
        self.assertTure(A)                               #assert A is ture
        self.assertIn(A,B)                               #assert A在B里面
        self.assertNotEqual                              #  !=
        self.assertFalse
        self.assertNotIn

    def test_negative_with_negative(self):
