import os
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class GetDriver:
    driver = None

    # 打开浏览器
    @classmethod
    def ger_driver(cls, browser_type='Edge'):
        # 变量接受当前文件所在文件夹位置
        dir_path = os.path.dirname(__file__)
        # 判断driver是否为None，为空的话需要打开浏览器
        if cls.driver is None:
            if browser_type == 'Edge':
                driver_path = os.path.join(dir_path, 'msedgedriver.exe')
                cls.driver = webdriver.Edge(executable_path=driver_path)
            elif browser_type == 'Chrome':
                driver_path = os.path.join(dir_path, 'chromedriver.exe')
                cls.driver = webdriver.Chrome(executable_path=driver_path)
            elif browser_type == 'Firefox':
                driver_path = os.path.join(dir_path, 'geckodriver.exe')
                cls.driver = webdriver.Firefox(executable_path=driver_path)
            else:
                print('很好奇你平时在用什么浏览器w(ﾟДﾟ)w')

        # 启动浏览器最大尺寸
        cls.driver.maximize_window()
        # 隐式等待10s
        cls.driver.implicitly_wait(10)

        # 调用登录方法
        GetDriver.login()

        # 停顿一会
        time.sleep(3)

        return cls.driver

    @classmethod
    def login(cls):
        cls.driver.get('http://192.168.163.131/smart_parking/')
        cls.driver.find_element_by_css_selector('input[placeholder="请输入用户名"]').clear()
        cls.driver.find_element_by_css_selector('input[placeholder="请输入用户名"]').send_keys('gf')
        cls.driver.find_element_by_css_selector('input[placeholder="请输入密码"]').clear()
        cls.driver.find_element_by_css_selector('input[placeholder="请输入密码"]').send_keys('vvv333')
        cls.driver.find_element_by_css_selector('input[placeholder="请输入验证码"]').clear()
        cls.driver.find_element_by_css_selector('input[placeholder="请输入验证码"]').send_keys('0000')
        cls.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/form/button[1]').click()

    @classmethod
    def wait_element_presence(cls, by, value, time_out=5):
        return WebDriverWait(cls.driver, time_out).until(lambda dr: dr.find_element(by, value))

    @classmethod
    def browser_close(cls):
        cls.driver.quit()
        cls.driver = None

if __name__ == '__main__':
    GetDriver().ger_driver()
