#coding=utf-8
import requests
import json
#上传文件
url = 'https://www.imooc.com/user/postpic'
requests.packages.urllib3.disable_warnings()
file = {
    "fileField":("视觉 - 9.jpg",open("C:/Users/HAN/Pictures/爱壁纸UWP/视觉/视觉 - 9.jpg","rb"),"image/jpeg"),
    "type":1
}
#cookie从哪里获取呢？
cookie = {  
    "PSEID":"311ea346f8a718ed77d7c8cac2332c56",
    "apsid":"MxOTk4ODQxZWEyZmQ2ODVmOGNkODA1OTM1OGE5ZmYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANDAyODAyNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxODMwMjE2NjAzN0AxNzMuY29tAAAAAAAAAAAAAAAAADhmODZkNzMwZDgyODA4YzJkNWI4MWI3ZDcyMzIxYmEz%2FwW9X%2F8FvV8%3DNW"
}
response = requests.post(url,files=file,cookies=cookie,verify = False).json()
print(json.dumps(response,indent=2,ensure_ascii=False))


'''
webfrom表单数据
Content-Disposition: form-data; name="fileField"; filename="视觉 - 9.jpg"
Content-Type: image/jpeg	<file>
Content-Disposition: form-data; name="type"	1
'''
