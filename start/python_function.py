#coding=utf-8
def people(age):
    #函数体
    if age>0:
        print("正常")
        name = get_name()
        print(name)
    else:
        print("不正常")

def get_name():
    return "张三"

people(10)