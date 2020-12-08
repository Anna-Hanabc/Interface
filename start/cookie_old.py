#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('https://www.imooc.com/')
element = driver.find_element_by_id("js-signin-btn")
element.click()
time.sleep(2)
driver.find_element_by_name('email').send_keys('18302166037')
driver.find_element_by_name('password').send_keys('hhh8023')
driver.find_element_by_xpath('//*[@id="signup-form"]/div[5]/input').click()
try:
    driver.find_element_by_xpath('//*[@id="index"]/div[12]/div/div/div/div/div[5]/div/a[2]').click()
except:
    pass
cookie_list = driver.get_cookies()
print(cookie_list)