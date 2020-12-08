#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('https://www.imooc.com/')
element = driver.find_element_by_id("js-signin-btn")
element.click()
time.sleep(2)

driver.find_element_by_name('email').send_keys('18302166037')
driver.find_element_by_name('password').send_keys('hhh8023')
driver.find_element_by_xpath('//*[@id="signup-form"]/div[5]/input').click()
time.sleep(2)

driver.get('https://www.imooc.com/user/setprofile')
time.sleep(2)
driver.find_elements_by_class_name('icon-note')[0].click()
driver.find_elements_by_class_name('moco-form-control')[7].find_elements_by_tag_name('option')[1].click()
#document.getElementsByClassName('moco-form-control')[7].value='7'

select_element = driver.find_elements_by_class_name('moco-form-control')[7]
Select(select_element).select_by_index(5)
Select(select_element).select_by_value('18')
Select(select_element).select_by_visible_text('Python工程师')

time.sleep(4)
driver.close()