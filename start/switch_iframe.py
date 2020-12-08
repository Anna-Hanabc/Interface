#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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

driver.get('http://www.imooc.com/wenda/save')
driver.switch_to.frame('ueditor_0')
time.sleep(2)
p_element = driver.find_element_by_tag_name('p')
ActionChains(driver).move_to_element(p_element).click().perform()
time.sleep(2)

driver.switch_to.default_content()#鼠标切到默认
time.sleep(2)
driver.find_elements_by_class_name('save-list-tag')[1].click()
time.sleep(3)
driver.close()