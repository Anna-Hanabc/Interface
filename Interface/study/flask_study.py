#coding=utf-8
from flask import Flask
from flask import request
import json
app = Flask(__name__)

#接口访问路径
@app.route('/')
#定义接口
def Home():
    return "hello world!"

@app.route('/get_login',methods=['GET'])
def get_login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username and password:
        data = {
            "username":username,
            "password":password,
            "code":"200",
            "message":"success",
            "info":"www.baidu.com"
        }
    else:
        data={
            "code":"404",
            "message":"parameter error"
        }
    return data

@app.route('/post_login',methods=['POST'])
def post_login():
    request_method = request.method
    username = request.form.get("username")
    password = request.form.get("password")
    if request_method == "GET":
        data={
            "code":"1",
            "message":"the request method is illegal"
        }
    elif username and password:
        data = {
            "username":username,
            "password":password,
            "code":"2",
            "message":"success",
            "info":"www.imooc.com"
        }
    else:
        data = {
            "code":"3",
            "message":"Please enter parameters"
        }
    return data
#模拟get请求
#url：https://www.imooc.com/passport/user/login?username=hhhan&password=1234567890
#返回：message，status，data

if __name__ == "__main__":
    app.run()