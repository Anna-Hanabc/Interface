#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
#from pykeyboard import PyKeyBoard#pyUserInput和pyHook没有安装成功
import time

driver = webdriver.Chrome()
#pykey = PyKeyBoard() #实例化
driver.get('chrome://settings/importData')

# 个人中心更换头像，标签input类型
# driver.get('https://www.imooc.com/')
# element = driver.find_element_by_id("js-signin-btn")
# element.click()
# time.sleep(2)
# driver.find_element_by_name('email').send_keys('18302166037')
# driver.find_element_by_name('password').send_keys('hhh8023')
# driver.find_element_by_xpath('//*[@id="signup-form"]/div[5]/input').click()
# time.sleep(2)
# driver.get('https://www.imooc.com/user/setprofile')
# time.sleep(5)
# driver.find_elements_by_class_name('js-avator-link')[0].click()
# driver.find_element_by_id('upload').send_keys('C:/Users/HAN/Pictures/爱壁纸UWP/动物/1.jpg')

#time.sleep(15)
#pykey.tab_key(pykey.shift_key)#所以先切换输入法
#pykey.type_string('C:/Users/HAN/Pictures/爱壁纸UWP/动物/1.jpg')#输入的是中文
#time.sleep(4)
#pykey.tab_key(pykey.enter_key)
#time.sleep(15)
#driver.close()