import time
from logging import Logger

from selenium.common import NoSuchElementException

from common.logger import Log
from page.page_login import PageLogin


class ProcessLogin:

    def __init__(self):
        self.login = PageLogin()
        self.logger = Log.get_logger()

    # 输入用户名
    def input_username(self, username):
        time.sleep(1)
        self.input(self.login.find_username(), username)
        self.logger.info(f'请输入用户名：{username}')

    # 输入密码
    def input_pwd(self, pwd):
        time.sleep(1)
        self.input(self.login.find_password(), pwd)
        self.logger.info(f'请输入密码：{pwd}')

    # 输入验证码
    def input_verifycode(self, verifycode):
        time.sleep(1)
        self.input(self.login.find_checkcode(), verifycode)
        self.logger.info(f'请输入验证码：{verifycode}')

    # 点击登录按钮
    def click_loginbtn(self):
        time.sleep(1)
        self.login.find_loginbtn().click()
        self.logger.info(f'点击登录按钮')

    # 公用input
    def input(self, el, content):
        el.clear()
        el.send_keys(content)

    # 判断登录前用户输入框是否存在
    def check_username(self):
        try:
            self.login.find_username()
            return True
        except NoSuchElementException:
            return False

    # 判断登录后页面用户名是否存在
    def login_text(self):
        el = self.login.find_welcome()
        if el:
            return el.text
        return ''

    # 获取登录失败弹窗文本
    def login_error_text(self):
        time.sleep(2)
        el = self.login.find_error()
        if el:
            return el.text

    # 登录失败点击确定
    def click_login_error_btn(self):
        time.sleep(5)
        el = self.login.find_error_btn()
        el.click()

    # 判断是否有弹窗
    def is_popups(self):
        el = self.login.find_error_btn()
        if el:
            return True
        return False




    # 注销登录
    def click_logout(self):
        self.login.find_logout().click()
