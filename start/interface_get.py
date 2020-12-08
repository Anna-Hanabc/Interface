#coding=utf-8
import requests
import urllib
import urllib2

url = "http://reg.haibian.com/login/ajax_login"
#定义请求数据，并赋值
data = {}
data['loginname'] = 'student08@qq.com'
data['password'] = '1111111'
#对请求数据编码
data = urllib.urlencode(data)
#数据和url连接
request = url+'?'+data
requestResponse = urllib3.urlopen(request)
responsestr = requestResponse.read()
responsestr = responsestr("unicode_escape")
print(responsestr)
'''
payload = {}
headers= {}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
'''