from selenium import webdriver
import requests
import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Common:
    driver = None
    session = None

    # 单例模式
    @classmethod
    def get_driver(cls, browser_type='edge'):
        if cls.driver is None:
            current_path = os.path.dirname(__file__)
            if browser_type == 'firefox' or browser_type == 'ff':
                driver_path = os.path.join(os.path.dirname(current_path),
                                           'driver/geckodriver.exe')
                cls.driver = webdriver.Firefox(executable_path=driver_path)
            elif browser_type == 'chrome' or browser_type == 'gc':
                driver_path = os.path.join(os.path.dirname(current_path),
                                           'driver/chromedriver.exe')
                cls.driver = webdriver.Chrome(executable_path=driver_path)
            elif browser_type == 'edge':
                driver_path = os.path.join(os.path.dirname(current_path),
                                           'driver/MicrosoftWebDriver.exe')
                cls.driver = webdriver.Edge(executable_path=driver_path)
            else:
                driver_path = os.path.join(os.path.dirname(current_path),
                                           'driver/IEDriverServer.exe')
                cls.driver = webdriver.Ie(executable_path=driver_path)
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(60)
        cls.driver.implicitly_wait(20)
        return cls.driver

    @classmethod
    def element_exist(cls, by, value):
        try:
            cls.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    @classmethod
    def wait_element_presence(cls, by, value, timeout=5):

        # for i in range(timeout):
        #     try:
        #         el = cls.driver.find_element(by, value)
        #         return el
        #     except NoSuchElementException:
        #         time.sleep(1)
        # return None
        # WebDriverWait(cls.driver, timeout).until(expected_conditions.presence_of_element_located((by, value))
        el = WebDriverWait(cls.driver, timeout).until(lambda dr: dr.find_element(by, value))
        return el

    @classmethod
    def wait_element_method(cls, method, timeout=5):
        return WebDriverWait(cls.driver, timeout).until(method)

    @classmethod
    def close_browser(cls):
        cls.driver.quit()
        cls.driver = None

    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.session = requests.session()
        return cls.session

    @classmethod
    def close_session(cls):
        cls.session.close()
        cls.session = None


if __name__ == '__main__':
    print(os.path.dirname(os.getcwd()))
    print(os.path.join(os.path.dirname(os.getcwd()), 'driver/geckodriver.exe'))
    print(os.getcwd())
