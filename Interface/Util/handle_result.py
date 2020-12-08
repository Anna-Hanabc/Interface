#coding=utf-8
# 校验errorCode/message/json格式/是否有某一字段
import openpyxl
import configparser
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
import json
from Util.handle_json import get_value

def handle_result(url,code):
    data = get_value(url,"/Config/code_message.json")
    if data != None:
        for i in data:
            message = i.get(code)
            if message:
                return message
            else:
                message = None
    return message

if __name__ == "__main__":
    print(handle_result("api3/beta4","1001"))

