#coding=utf-8
import openpyxl
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
import configparser

file_path = base_path + "/Config/server.ini"
print(file_path)
cf = configparser.ConfigParser()
cf.read(file_path)
data = cf.get("server","host")
print(data)

class HandleInit:
    def load_ini(self):
        file_path = base_path + "/Config/server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding="utf-8-sig")
        return cf
    def get_value(self,key,section=None):
        '''
        获取ini的value
        '''
        cf = self.load_ini()
        if section == None:
            section = "server"
        try:
            data = cf.get(section,key)
        except Exception:
            print("获取不到section下的value")
            data = None
        return data

handle_ini = HandleInit()

if __name__ == "__main__":
    hi = HandleInit()
    data = hi.get_value("username","server")
    print(data)