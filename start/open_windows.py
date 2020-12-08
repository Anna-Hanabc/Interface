#coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
from selenium.webdriver.support import expected_conditions as EC

driver.get('https://www.imooc.com/user/newlogin/from_url')
driver.find_element_by_name('email').send_keys('18302166037')
driver.find_element_by_name('password').send_keys('hhh8023')
driver.find_element_by_xpath('//*[@id="signup-form"]/div[5]/input').click()
time.sleep(2)

driver.get('https://www.imooc.com/user/setbindsns')
driver.find_elements_by_class_name('inner-i-box')[1].find_element_by_class_name('moco-btn-normal').click()

handle_list = driver.window_handles
current_handle = driver.current_window_handle

print(handle_list)
#[1,2,3,4]
time.sleep(15)

for i in handle_list:
    if i != current_handle:
        driver.switch_to.window(i)
        title = EC.title_contains('网站链接')
        if title(driver) == True:
            break

time.sleep(5)
driver.find_element_by_id('jump_login_url_a').click()
driver.find_element_by_id('username').send_keys('test')
time.sleep(5)

driver.close()