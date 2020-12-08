#coding=utf-8
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
prefs = {'download.default_directory':'C:\\Users\\HAN\\Downloads','profile.default_content_settings.popups':0}
options.add_experimental_option('prefs',prefs)

driver = webdriver.Chrome(options = options)
driver.get('https://www.imooc.com/mobile/app')
driver.find_element_by_xpath('//*[@id="main"]/div[1]/a[2]').click()
time.sleep(5)
driver.close()