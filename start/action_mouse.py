#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.imooc.com')
element = driver.find_element_by_class_name("menuContent").find_elements_by_class_name('item')[5]
ActionChains(driver).move_to_element(element).perform()

time.sleep(3)
driver.find_elements_by_class_name("tag-box")[6].find_element_by_link_text("自动化测试").click()
time.sleep(3)
driver.close()