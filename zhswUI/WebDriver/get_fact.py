from selenium import webdriver
from util.config import host_port
import time

'''
单例模式：让这个类只有一个实例化对象
在UI自动化测试中解决，打开多个浏览器的问题，让所有的用例都在同一个浏览器上执行
'''


class GetFact():

    # 定义一个静态属性，保存生成的浏览器对象
    driver = None

    @classmethod
    def get_driver(cls, browser_type="Edge"):
        # 判断 如果driver为None 则需要打开浏览器，将打开的浏览器对象赋值给静态属性driver
        if cls.driver is None:
            # 打开浏览器的时候，需要进行判断，打开的是那个浏览器
            if browser_type == "Chrome":
                cls.driver = webdriver.Chrome()
            elif browser_type == "Firefox":
                cls.driver = webdriver.Firefox()
            elif browser_type == "Edge":
                cls.driver = webdriver.Edge()
            else:
                print("浏览器类型不支持")

            # 直接设置浏览器最大化
            cls.driver.maximize_window()
            # 隐式等待
            cls.driver.implicitly_wait(10)

            # 调用登录的方法
            GetFact.login()

            # 登录之后，稍稍停顿一下
            time.sleep(3)

        return cls.driver

    @classmethod
    def login(cls):
        # 打开网页
        cls.driver.get(f"http://{host_port}/water/#/login")
        # 输入用户名
        cls.driver.find_element_by_css_selector("#fm > div:nth-child(3) > div > div > input").send_keys("admin")
        # 输入密码
        cls.driver.find_element_by_css_selector("#fm > div:nth-child(4) > div > div > input").send_keys("123")
        # 点击 登录 按钮
        cls.driver.find_element_by_css_selector('#btuLogin > span').click()


if __name__ == '__main__':
    GetFact.get_driver()