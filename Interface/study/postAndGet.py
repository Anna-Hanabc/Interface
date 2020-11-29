#coding=utf-8
import requests
import json
'''忽略https报错'''
requests.packages.urllib3.disable_warnings()
post_url = 'https://www.imooc.com/search/hotwords'
'''python中小括号代表元组 （1，2，3，4）;大括号代表字典'''
data = {}
'''不验证https，可以加参数：verify = False'''
response_post = requests.post(post_url,data,verify = False).json()
'''返回以json格式化处理.dumps:json转义；ident缩进；禁止ascii码转义'''
print(json.dumps(response_post,indent=2,ensure_ascii=False))

get_url = 'https://www.imooc.com/activity/newcomer'
response_get = requests.get(get_url,verify = False).json()
print(json.dumps(response_get,indent=2,ensure_ascii=False))