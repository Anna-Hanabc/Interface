#coding=utf-8
import requests 
import json
import time
# from selenium import webdriver
class requests_webdriver:
    def __init__(self):
        self.driver = self.chrome_driver()
    def chrome_driver(self):
        url = 'http://127.0.0.1:4444/wd/hub/session/'
        #json.dumps 把json转换成字符串
        data = json.dumps({
            'desiredCapabilities':{
                'browserName':'chrome'
            }
        })
        Response = requests.post(url,data).json()
        session = Response['sessionId']
        driver = url + session
        print(session)
        print(driver)
        return driver

    def get_url(self,url):
        base_url = self.driver+'/url'
        data = json.dumps({
            "url":url
        })
        requests.post(base_url,data)

    def find_element_by_id(self,value):
        base_url = self.driver+'/element'
        data = json.dumps({
            "using":'name',
            #定位方式不同只需要更换using后的参数即可
            #"using":'id',
            "value":value
        })
        #先打印jison串，得到返回中element定位值，返回出去
        response = requests.post(base_url,data).json()['value']['element-6066-11e4-a52e-4f735466cecf']
        print(response)
        return response

if __name__ == '__main__':
    request_driver = requests_webdriver()
    request_driver.get_url('http://www.imooc.com/user/newlogin')
    request_driver.find_element_by_id('email')
