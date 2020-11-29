#coding=utf-8
import requests
import json
#下载apk文件
url = 'http://file.mukewang.com/apk/app/124/1606182011/imooc_7.4.4_10102001_android.apk?version=1606182013'
response = requests.get(url,verify = False)
with open ("C:/Users/HAN/.vscode/Interface/study/mukewang.apk","wb") as f:
    f.write(response.content)
print(response)
