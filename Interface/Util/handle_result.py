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
from deepdiff import DeepDiff

def handle_result(url,code):
    data = get_value(url,"/Config/code_message.json")
    # print('---->',code,'---->',type(code))
    # print(data)
    # [{'1001': '登陆成功'}, {'1002': '用户名错误'}, {'1003': '密码错误'}]
    # 这里为什么返回None呢
    if data != None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None

def handle_result_json(dict1,dict2):
    '''
    校验json格式：pip install deepdiff
    '''
    # 校验入参是否是字典
    if isinstance(dict1,dict) and isinstance(dict2,dict):
        cmp_dict = DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        # print(cmp_dict)
        if cmp_dict.get("dictionary_item_added") or cmp_dict.get("dictionary_item_removed"):
            return False
        else:
            return True
    return False

def get_result_json(url,status):
    data = get_value(url,"/Config/result.json")
    if data != None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None

if __name__ == "__main__":
    # print(handle_result("api3/beta4","1001"))
    # print(handle_result_json(dict1,dict2))
    # print(get_result_json("api3/newcourseskill","sucess"))
    pass
