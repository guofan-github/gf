from selenium.webdriver.common.by import By

from common.common import Common


class PageLogin:

    def __init__(self):
        self.driver = Common.get_driver()

    # 用户名定位
    def find_username(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, 'input[placeholder="请输入用户名"]')

    # 密码定位
    def find_password(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, 'input[placeholder="请输入密码"]')

    # 验证码定位
    def find_checkcode(self):
        return Common.wait_element_presence(By.XPATH,
                                            '//*[@id="app"]/div/div[1]/div/div[2]/form/div[3]/div/div[1]/input')

    # 登录按钮定位
    def find_loginbtn(self):
        return Common.wait_element_presence(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/form/button[1]')

    # 登录成功显示用户名
    def find_welcome(self):
        logintext_path = '#app > section > section > aside > ul > h1'
        is_login = Common.wait_element_method(lambda dr:
                                              dr.find_element_by_css_selector(logintext_path).text == '首页')
        if is_login:
            return Common.wait_element_presence(By.CSS_SELECTOR, logintext_path)
        return None

    # 登录测试错误时弹窗
    def find_error(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, 'body > div.el-overlay.is-message-box > div > div.el-message-box__content > div.el-message-box__container > div > p')

    # 登录测试错误弹窗确定按钮
    def find_error_btn(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, 'body > div.el-overlay.is-message-box > div > div.el-message-box__btns > button')

    # 注销按钮定位
    def find_logout(self):
        return Common.wait_element_presence(By.XPATH, '/html/body/div[1]/section/header/div[2]/div[5]/i/svg')