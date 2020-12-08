#coding=utf-8
import configparser
class ReadIni:
    def __init__(self):
        self.data = self.load_ini()

    def load_ini(self):
        cf = configparser.ConfigParser()
        cf.read('C:/Users/HAN/.vscode/start/config/LocalElement.ini')
        return cf

    def get_value(self,key):
        print('---->',key)
        return self.data.get('element',key)

read_ini = ReadIni()
