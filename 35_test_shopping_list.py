import unittest
from shopping_list import ShoppingList
class TestShoppingList(unittest.TestCase):        #继承自unittest这个库里面的TestCase类
    def setUp(self):
        self.shopping_list = ShoppingList({"纸巾":8,"帽子":30,"拖鞋":15})
    def test_get_item_count(self):            #一定要test_ 开头。才能被当做测试用例  #计算数目
        self.assertEqual(self.shopping_list.get_item_count(),3)
    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 55)

#终端terminal 输入：Python -m unittest
#测试结构 多少个···就多少个测试用例通过了   F表示没过