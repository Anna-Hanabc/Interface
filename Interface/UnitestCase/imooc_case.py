#coding=utf-8
#导入自己的包，必须添加以下几行
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Base.base_request import request
import requests
import unittest
import json
import mock
import HTMLTestRunner

def read_json():
    with open(base_path + "/Conifg/user_data.json") as f:
        data = json.load(f)
        return data

def get_value(key):
    data = read_json()
    return data[key]

host = "http://www.imooc.com"
class ImoocCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("case类开始执行")
    
    @classmethod
    def tearDownClass(cls):
        print("case类执行结束")

    def test_getbanner(self):
        url = host + "api3/getbanneradvertyer2"
        data = {}
        mock_method = mock.Mock(return_value = get_value("api3/getbanneradvertyer2"))
        request.run_main = mock_method
        res = request.run_main("post",url,data)
        # print(json.dumps(res))
        self.assertEqual(res["v"],7)

    def test_beta4(self):
        url = host + "api3/beta4"
        data = {}
        mock_method = mock.Mock(return_value = get_value("api3/beta4"))
        request.run_main = mock_method
        res = request.run_main("post",url,data)
        self.assertEqual(res["id"],"1")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [ImoocCase("test_getbanner"),ImoocCase("test_beta4")]
    suite.addTests(tests)
    file_path = base_path + "/Report/report.html"
    with open(file_path,"wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is a test", description="hhhan test")
        runner.run(suite)
    f.close()
