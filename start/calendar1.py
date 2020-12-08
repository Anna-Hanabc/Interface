#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('一个日历脚本的地址，日历为text格式')

# 通过js移除text的只读属性
js = 'document.getElementById("layDateInput").removeAttribute("readonly");'
driver.execute_script(js)
element = driver.find_element_by_id('laydateInput')
element.clear()
#删除placeholer
element.send_keys('2020-10-27')
time.sleep(5)
driver.close()