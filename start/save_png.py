#coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.imooc.com")
driver.save_screenshot('test.png')
time.sleep(2)
driver.close()