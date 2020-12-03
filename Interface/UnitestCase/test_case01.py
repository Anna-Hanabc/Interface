#coding=utf-8
import requests
import unittest

#导入自己的包，必须添加以下几行
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Base.base_request import request

url = "http://www.baidu.com"
data = {
    "username":"1111",
    "password":"2222"
}
host = "http://www.imooc.com"
class TestCase01(unittest.TestCase):
    # def setUp(self):
    #     print("case开始执行")

    # def tearDown(self):
    #     print("case执行结束")

    #类方法
    @classmethod
    def setUpClass(cls):
        print("case类开始执行")
    
    @classmethod
    def tearDownClass(cls):
        print("case类执行结束")

    def test_01(self):
        print("case01")
        data1 = {
            "user":"1111"
        }
        self.assertDictEqual(data1,data,msg="字典不相等")

    def test_02(self):
        print("case02")
        data1 = {
            "username":"1111",
            "password":"2222"
        }
        self.assertDictEqual(data1,data,msg="字典不相等")
        
    def test_03(self):
        print("case03")
        flag = True
        self.assertFalse(flag)

    def test_04(self):
        res = request.run_main("get",url,data)
        print(res)

    #条件为真，不执行。常用于环境判断，条件判断
    @unittest.skipIf(host!="http://www.imooc.com","case不执行")
    def test_05(self):
        print("case05")
        flag = "111"
        flag1 = "222"
        self.assertEqual(flag,flag1,msg="字符串不相等")

    @unittest.skip("该case不执行")
    def test_06(self):
        print("case06")
        flag = "fggjjprogwe"
        s = "fgga"
        self.assertIn(s,flag,msg="子串不在主串中")

if __name__ == "__main__":
    # 执行顺序：case编号顺序
    # unittest.main()

    suite = unittest.TestSuite()

    # 执行顺序：测试套件顺序
    # suite.addTest(TestCase01("test_06"))
    # suite.addTest(TestCase01("test_03"))
    # suite.addTest(TestCase01("test_02"))

    # 执行顺序：test case 中的case顺序
    tests = [TestCase01("test_04")]
    # tests = [TestCase01("test_04"),TestCase01("test_03"),TestCase01("test_02")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
    



'''
case执行顺序是这样子的，点代表执行成功
case类开始执行
    case开始执行
    case01
    case执行结束
    .case开始执行
    case02
    case执行结束
    .case开始执行
    case03
    case执行结束
.case类执行结束

真实的执行顺序：不是代码顺序，而是case编号顺序；或者测试套件TestSuite的顺序
'''