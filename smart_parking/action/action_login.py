import time

from common.common import Common
from procrss.process_login import ProcessLogin


class ActionLoginUI:

    def __init__(self):
        self.driver = Common.get_driver()
        self.login = ProcessLogin()

    # 进入首页
    def do_homepage(self):
        self.driver.get("http://192.168.163.131/smart_parking")

    # 登录
    def do_login(self, user, pwd, code):
        self.login.input_username(user)
        self.login.input_pwd(pwd)
        self.login.input_verifycode(code)
        self.login.click_loginbtn()

    # 注销
    def logout(self):
        self.login.click_loginbtn()



