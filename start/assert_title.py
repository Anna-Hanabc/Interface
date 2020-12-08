#coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://www.imooc.com/")
title_name = driver.title
print(title_name)

if '慕课网' in title_name:
    print("打开正确")
else:
    print("打开错误")

titleis = EC.title_is('慕课网')
print(titleis(driver))
titlecontains = EC.title_contains('慕课网')
print(titlecontains(driver))