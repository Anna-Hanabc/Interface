#coding=utf-8
import sys
import time
sys.path.append('C:/Users/HAN/.vscode/start')
from read_init import ReadIni
from open_browser import SeleniumDriver
read_ini = ReadIni()
seleniun_driver = SeleniumDriver('chrome')

data = read_ini.get_value('username')
data_info = data.split(',')
by = data_info[0]
local = data_info[1]
print(by)
print(local)

seleniun_driver.get_url('http://www.imooc.com/user/newlogin')
time.sleep(2)
seleniun_driver.send_value(by,local,"hhhan")
time.sleep(3)
seleniun_driver.close_driver()