#coding=utf-8
import requests
import unittest

url = "http://www.imooc.com"
data = {
    "username":"1111",
    "password":"2222"
}

class TestCase02(unittest.TestCase):
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
        print("case04")
        flag = True
        self.assertTrue(flag)

    def test_05(self):
        print("case05")
        flag = "111"
        flag1 = "222"
        self.assertEqual(flag,flag1,msg="字符串不相等")

    def test_06(self):
        print("case06")
        flag = "fggjjprogwe"
        s = "fgga"
        self.assertIn(s,flag,msg="子串不在主串中")

