#coding=utf-8
import requests
import urllib
import urllib2

url = "http://xapi.kybyun.com/user/login"
data = {}
data['loginname'] = 'student08@qq.com'
data['password'] = '1111111'
#数据编码及赋值
data = urllib.urlencode(data)
req = urllib2.Request(url,data)
#打开地址并赋值给变量
responseStr = urllib2.urlopen(req)
#读取获得的值
responseStr = responseStr.read()
#将获得的结果转码
responseStr = responseStr.decode("unicode_escape")
print(responseStr)