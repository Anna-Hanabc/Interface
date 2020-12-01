#coding=utf-8
import mock
import requests
import unittest

url = "http://www.imooc.com"
data = {
    "username":"hhhan",
    "password":"123"
}
def post_request(url,data):
    res = requests.post(url,data=data).json()
    return res

def get_request(url,data):
    #url = "http://www.imooc.com/login/register?user=111&pass=222"
    res = requests.get(url,params=data).json()
    return res

class TestLogin(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case执行结束")

    def test_01(self):
        data = {
            "username":"111111"
        }
        response = mock.Mock(return_value=data)
        print(data)
        self.assertLessEqual("111111",response())

if __name__ == "__main__":
    unittest.main()