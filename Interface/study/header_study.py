#coding=utf-8
import requests
import json
import hashlib
#假设网站加密有一个基础值
imooc = "imooc.com"
#引入md5哈希加密
md5 = hashlib.md5()
#基础值必须转码，不转码会出错
md5.update(imooc.encode('utf-8'))
res = md5.hexdigest()
print(res)

#可能加密不止一次，比如和请求数据一起再md5一次
data = str( {
    "user":"hhhan"
})
#转码对象必须是字符串，所以把字典强转成字符串
md5.update(data.encode('utf-8'))
res1 = md5.hexdigest()
print(res1)

header = {
    'Host':'m.imooc.com',
    'Connection':'keep-alive',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer':'https://m.imooc.com/',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'token':res1
}
url = 'http://www.imooc.com'

#转换成json时，会有json解析错误，直接从fillder中看请求的token是否正确就可以了
#response = requests.get(url,headers=header,verify=False).text
#print(response)
