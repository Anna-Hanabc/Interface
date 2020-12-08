#coding=utf-8
from selenium import webdriver
import time
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
#from pykeyboard import PyKeyBoard#pyUserInput和pyHook没有安装成功
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
sys.path.append('C:/Users/HAN/.vscode/start')
from read_init import read_ini
from handle_json import handle_json

#类使用
class SeleniumDriver:
    
    def __init__(self,browser):
        self.driver = self.open_browser(browser)

    def open_browser(self,browsername):
        try:
            if browsername == 'chrome':
                #下载位置初始化配置
                options = webdriver.ChromeOptions()
                prefs = {'download.default_directory':'C:\\Users\\HAN\\Downloads','profile.default_content_settings.popups':0}
                options.add_experimental_option('prefs',prefs)
                driver = webdriver.Chrome(options = options)
            elif browsername == 'firefox':
                profile = webdriver.FirefoxProfile()
                profile.set_preference('browser.download.dir','C:\\Users\\HAN\\Downloads')
                profile.set_preference('browser.download.folderList',2)
                profile.set_preference('browser.helpApps.neverAsk.saveToDisk','application/zip')
                driver = webdriver.Firefox(firefox_profile = profile)
            elif driver == 'ie':
                driver = webdriver.Ie()
            else:
                driver = webdriver.Edge()
            #time.sleep(3)
            driver.maximize_window()
            return driver
        except:
            print('打开浏览器失败')
            return None

    def get_url(self,url):
        #driver = open_browser('chrome')
        if self.driver != None:
            self.driver.maximize_window()
            if 'http://' in url:
                self.driver.get(url)
            elif 'C:' in url:#本地地址
                self.driver.get(url)
            else:
                print('url不正确')
        else:
            print('case失败')
        #self.driver.quit()

    def handle_windows(self,*args):
        #self.driver = open_browser('chrome')
        value = len(args)
        if value == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.driver.minimize_window()
            elif args[0] == 'back':
                self.driver.back()
            elif args[0] == 'go':
                self.driver.forward
            elif args[0] == 'refresh':
                self.driver.refresh()
        elif value == 2:
            self.driver.set_window_size(args[0],args[1])
        else:
            print('参数有误')
        #time.sleep(2)
        #self.driver.quit()

    def assert_title(self,title_name=None):
        #判断title是否正确
        if title_name != None:
            get_title = EC.title_contains(title_name)
            return get_title(self.driver)

    def open_url_is_true(self,url,title_name=None):
        #通过title判断页面是否正确
        self.get_url(url)
        return self.assert_title(title_name)

    def close_driver(self):
        self.driver.close()

    def switch_windows(self,title_name=None):
        #切换窗口
        handle_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        print(handle_list)
        for i in handle_list:
            if i != current_handle:
                time.sleep(1)
                self.driver.switch_to.window(i)
                if self.assert_title(title_name):
                    break
        time.sleep(2)

    def element_isdisplay(self,element):
        flag = element.is_displayed()
        if flag == True:
            return element
        else:
            return False

    def get_element(self,info):
        #获取元素element
        #@parame by 定位方式
        #@parame value 定位值
        #@return element 返回元素
        #@info为配置文件中写的[by，value]list
        by,value = self.get_local_element(info)
        element = None
        try:
            if by == 'id':
                element = self.driver.find_element_by_id(value)
                self.element_isdisplay(element)
            elif by == 'name':
                element = self.driver.find_element_by_name(value)
            elif by == 'css':
                element = self.driver.find_element_by_css_selector(value)
            elif by == 'class':
                element = self.driver.find_element_by_class_name(value)
            else:
                element = self.driver.find_element_by_xpath(value)
        except:
            print("定位方式：",by,"，定位值：",value,"，定位出现错误，没有定位成功")
        return self.element_isdisplay(element)

    def get_elements(self,info):
        #获取元素elements
        #@parame by 定位方式
        #@parame value 定位值
        #@return elements 返回一个元素list
        elements = None
        element_list = []
        by,value = self.get_local_element(info)
        if by == 'id':
            elements = self.driver.find_elements_by_id(value)
        elif by == 'name':
            elements = self.driver.find_elements_by_name(value)
        elif by == 'css':
            elements = self.driver.find_elements_by_css_selector(value)
        elif by == 'class':
            elements = self.driver.find_elements_by_class_name(value)
        else:
            elements = self.driver.find_elements_by_xpath(value)
        
        for element in elements:
            if self.element_isdisplay == False:
                continue
            else:
                element_list.append(element) 
        return element_list

    def get_level_element(self,info_level,node_info):
        #层级定位
        #父节点
        #根据父节点找子节点
        element = self.get_element(info_level)
        node_by,node_value = node_info
        if element == False:
            return False
        if node_by == 'id':
            node_element = element.find_element_by_id(node_value)
        elif node_by == 'name':
            node_element = element.find_element_by_name(node_value)
        elif node_by == 'css':
            node_element = element.find_element_by_css_selector(node_value)
        elif node_by == 'class':
            node_element = element.find_element_by_class_name(node_value)
        else:
            node_element = element.find_element_by_xpath(node_value)
        return self.element_isdisplay(node_element)

    def get_list_element(self,info,index):
        #通过list定位元素
        elements = self.get_elements(info)
        if index > len(elements):
            return None
        else:
            return elements[index]

    def send_value(self,info,key):
        #输入值
        element = self.get_element(info)
        if element == False:
            return ("输入失败，定位元素没有展示")
        else:
            if element != None:
                element.send_keys(key)
            else:
                print("定位元素不可见，输入失败")

    def click_element(self,info):
        #点击元素
        element = self.get_element(info)
        if element != False:
            if element != None:
                element.click()
            else:
                print("定位元素无法找到，点击失败")
        else:
            print("定位元素不可见，点击失败")

    def check_box_isselected(self,info,check=None):
        '''
        判断是否选中
        '''
        if element != False:     
            element = self.get_element(info)
            flag = element.is_selected()
            if flag == True:
                if check != 'check':
                    self.click_element(info)
            else:
                if check == 'check':
                    self.click_element(info)
        else:
            print("定位元素不可见，无法选中")

    def get_local_element(self,info):
        data = read_ini.get_value(info)
        data_info = data.split(',')
        return data_info

    def get_selected(self,info,vaule_index,index=None):
        '''
        通过index获取选择对象，然后选中selected
        '''
        selected_element = None
        if index != None:
            selected_element = self.get_list_element(info,index)
        else:
            selected_element = self.get_element(info)
        Select(selected_element).select_by_index(vaule_index)
    
    '''
    #pyUserInput和pyHook没有安装成功
    def upload_file(self,file_name):
        #非input类型上传文件
        #@parme filename上传路径
        pykey = PyKeyBoard() #实例化
        pykey.tab_key(pykey.shift_key)#所以先切换输入法
        pykey.type_string('file_name')#输入的是中文
        time.sleep(2)
        pykey.tab_key(pykey.enter_key)
    '''

    def upload_file_function(self,file_name,info,send_info=None):
        element = self.get_element(info)
        if element.tag_name == 'a':
            #element = driver.find_element_by_xpath("//a[@class='avator-btn-fake']/following-sibling::input[1]")
            #self.get_element(inf0)
            self.send_value(send_info,file_name)
        else:
            self.click_element(info)
            #self.upload_file(file_name)

    def download_file(self,info):
        '''
        下载文件,初始化浏览器配置在open_browser方法中
        '''
        self.click_element(info)

    def js_excute_calender(self,info):
        local = self.get_local_element(info)
        by = local[0]
        value = local[1]
        if by == 'id':
            by_key = 'getElementById'
        elif by == 'class':
            by_key = 'getElementByClassName'
        js = 'document.%s("%s").removeAttribute("readonly");'%(by_key,value)
        self.driver.execute_script(js)

    def calender(self,info,value):
        '''
        修改日历
        '''
        element = self.get_element(info)
        try:
            element.get_element(info).get_attribute('readonly')
            self.js_excute_calender(info)
        except:
            print("当前不是只读属性日历")
        element.clear()
        self.send_value(info,value)
        
    def moveto_element_mouse(self,info):
        '''
        移动鼠标到指定元素
        '''
        element = self.get_element(info)
        ActionChains(self.driver).move_to_element(element).perform()

    def ctrl_f5(self):
        '''
        强制刷新ctrl+f5：按住control，按住f5，释放掉，提交操作
        '''
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()

    def switch_iframe(self,info=None):
        '''
        切换iframe：有定位信息时切入，没有时切出
        '''
        if info != None:
            iframe_element = self.get_element(info)
            self.driver.switch_to.frame(iframe_element)
        else:
            self.driver.switch_to.default_content()

    def switch_alert(self,info,value=None):
        '''
        浏览器系统级弹窗
        @prame info 确认或取消
        @praame value 输入值
        '''
        Windows_alert = self.driver.switch_to.alert
        if info == 'accept':
            if value ==None:
                Windows_alert.accept()
            else:
                Windows_alert.send_keys('value')
                Windows_alert.accept()
        else:
            Windows_alert.dismiss()

    def scroll_get_element(self,list_info,str_info):
        '''
        滑动查找元素
        执行js中参数应该为一屏的大小
        '''
        t = True
        list_element = self.get_elements(list_info)
        js = 'document.documentElement.scrollTop=1000;'
        while t:
            for element in list_element:
                title_name = element.find_element_by_tag_name('p').text
                if title_name in str_info:
                    element.click()
                    t = False
            self.driver.execute_script(js)
            time.sleep(3)
    
    def scroll_element(self,info):
        '''
        滑动查找元素升级版
        执行js中参数应该为一屏的大小
        '''
        js = 'document.documentElement.scrollTop=1000;'
        t = True
        while t:
            try:
                self.get_element(info)
                t = False
            except:
                self.driver.execute_script(js)
        
    def get_cookie(self):
        '''
        获取cookie
        一般通过接口或依赖实现
        '''
        cookie = self.driver.get_cookies()
        handle_json.write_data(cookie)


    def set_cokkies(self):
        '''
        植入cookie
        '''
        self.driver.delete_all_cookies()
        time.sleep(1)
        cookie = handle_json.get_data()
        self.driver.add_cookie(cookie)
        time.sleep(1)

    def save_png(self):
        now_time = time.strftime("%Y%m%d%H%M%S")
        self.driver.get_screenshot_as_file('%s.png' %now_time)


selenium_driver = SeleniumDriver('chrome')
selenium_driver.handle_windows('max')
'''
selenium_driver.open_url_is_true('http://www.imooc.com/','慕课网')
print(selenium_driver.open_url_is_true('http://www.imooc.com/','慕课网'))
selenium_driver.switch_windows('慕课网')
'''
selenium_driver.get_url('http://www.imooc.com/user/newlogin')
selenium_driver.save_png()
'''
selenium_driver.get_element('username')
selenium_driver.send_value('username','abc')
selenium_driver.send_value('password','test')
selenium_driver.click_element('loginbutton')
'''
#关闭浏览器！！！
time.sleep(2)
selenium_driver.close_driver()