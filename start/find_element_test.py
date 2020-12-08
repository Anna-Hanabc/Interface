#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.imooc.com/')
element = driver.find_element_by_id("js-sing-btn")
element.click()
EC.presence_of_element_located
'''
LOCATOR = (By,ID,'username')
EC.visibility_of_element_located(LOCATOR)
'''

driver.find_element_by_name('email').send_keys('18302166037')
driver.find_element_by_name('password').send_keys('hhh8023')
driver.find_element_by_xpath('//*[@id="signup-form"]/div[5]/input').click()
#登录按钮可以用css层级定位
#driver.find_elements_by_css_selector(".rlf-group>.moco-btn").click()
time.sleep(2)
#浏览器console中输入：document.getElementsByName('password')[0]可查看元素
#element = driver.find_element_by_name('password')[0]
#element.send_keys('test')

#driver.find_element_by_link_text('Unity3d粒子系统射击特效')
#driver.find_element_by_partial_link_text('Unity3d').click()
#elements时需要加下标
#driver.find_elements_by_partial_link_text()[]

#根据list定位
driver.get('https://www.imooc.com/user/setbindsns')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/ul/li[2]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="setting-profile"]/div[2]/a').click()
time.sleep(2)
driver.find_elements_by_id("nick")[1].send_keys('abc')

#切换到焦点
driver.get('https://www.imooc.com/wenda/save')
time.sleep(2)
driver.switch_to_active_element().send_keys('test')
time.sleep(4)
driver.close()

#css定位:标签（尖括号后的单词，比如button，div，input）；id（#）；class（.）
# driver.find_elements_by_css_selector(".imv2-search2")

