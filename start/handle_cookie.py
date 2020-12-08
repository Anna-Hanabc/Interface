#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('https://order.imooc.com/myorder')
time.sleep(2)
driver.delete_all_cookies()
time.sleep(2)
cookie_list = {
    'domain': '.imooc.com', 
    #'expiry': '1605051385',  如果expiry在cookie中，需要删掉不然会报错
    'httpOnly': False, 
    'name': 'apsid', 
    'path': '/', 
    'secure': False, 
    'value': 'MxOTk4ODQxZWEyZmQ2ODVmOGNkODA1OTM1OGE5ZmYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANDAyODAyNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxODMwMjE2NjAzN0AxNzMuY29tAAAAAAAAAAAAAAAAADYwN2YxZWM1ODlmNjFmNmExNGU0NDEzYzQ1OGRmYzNkouihX6LooV8%3DNW'
}
driver.add_cookie(cookie_list)
time.sleep(2)
driver.get('https://order.imooc.com/myorder')
time.sleep(2)
driver.close()

