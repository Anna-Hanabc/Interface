#coding=utf-8
#浏览器级别的弹窗，无法定位
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('file://C:/test.html')
time.sleep(2)

driver.find_element_by_id('alert').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element_by_id('sure').click()
time.sleep(2)
driver.switch_to.alert.accept()
driver.refresh()
time.sleep(1)
driver.find_element_by_id('sure').click()
time.sleep(2)
driver.switch_to.alert.dismiss()
driver.refresh()

driver.find_element_by_id('three').click()
time.sleep(2)
alert_element = driver.switch_to.alert
print(alert_element.text)
alert_element.send_keys('test')
driver.switch_to.alert.accept()
time.sleep(1)
driver.refresh()

driver.close()