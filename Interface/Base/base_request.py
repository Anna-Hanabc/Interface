#coding = utf-8
import requests
import json
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_init import handle_ini
from Util.handle_json import get_value

class BaseRequest:
    def send_post(self,url,data):
        '''
        发送post请求
        '''
        res = requests.post(url=url,data=data).text
        return res
    
    def send_get(self,url,data):
        '''
        发送get请求
        '''
        res = requests.get(url=url,params=data).text
        return res

    def run_main(self,method,url,data):
        '''
        执行方法，传递method，url，data参数
        '''
        # return get_value(url)
        base_url = handle_ini.get_value("host")
        if 'http' not in url:
            url = base_url + url
        if method == "get":
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        try:
            res = json.loads(res)
        except:
            print("结果是text，解析失败")
        return res

request = BaseRequest()
if __name__ == "__main__":
    request = BaseRequest()
    request.run_main("post","http://www.baidu.com.login","{'username':'123'}")