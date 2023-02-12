import time

from faker import Faker

from common.logger import Log
from page.page_rights_management import PageRightsManagement


class ProcessRightsManagement:

    def __init__(self):
        self.process = PageRightsManagement()
        self.logger = Log.get_logger()

    # 点击权限管理
    def click_rights_management(self):
        self.process.find_rights_management().click()
        self.logger.info('点击权限管理')
        time.sleep(2)

    # 点击账号管理
    def click_account_management(self):
        self.process.find_account_management().click()
        self.logger.info('点击账号管理')

    # 点击新增按钮
    def click_add_bwn(self):
        self.process.find_add_bwn().click()
        self.logger.info('点击新增按钮')

    # 公用输入
    def input(self, el, concent):
        el.clear()
        el.send_keys(concent)

    # 输入账号
    def input_account(self, account):
        self.input(self.process.find_account_input(), account)
        self.logger.info(f'输入账号：{account}')

    # 输入密码
    def input_password(self, password):
        self.input(self.process.find_password_input(), password)
        self.logger.info(f'输入密码：{password}')

    # 再次输入密码
    def reinput_password(self, password):
        self.input(self.process.find_password_reinput(), password)
        self.logger.info(f'再次输入密码：{password}')

    # 输入电话
    def input_tel(self, tel):
        self.input(self.process.find_tel_input(), tel)
        self.logger.info(f'输入电话：{tel}')

    # 输入姓名
    def input_name(self, name):
        self.input(self.process.find_name_input(), name)
        self.logger.info(f'输入姓名：{name}')
        time.sleep(1)

    # 点击选择角色下拉框
    def click_role_box(self):
        self.process.find_role_input().click()
        self.logger.info('点击选择角色下拉框')
        time.sleep(2)

    # 点击角色
    def click_role(self):
        self.process.find_role().click()
        self.logger.info('点击选择角色')
        time.sleep(2)

    # 收回下拉框点击
    def click_recover(self):
        self.process.find_account_input().click()
        self.logger.info('点击账号输入栏，收回选择角色下拉框')
        time.sleep(1)

    # 点击启用
    def click_enable(self):
        self.process.find_enable().click()
        self.logger.info('点击启用')
        time.sleep(2)

    # 点击保存
    def click_save(self):
        self.process.find_save().click()
        self.logger.info('点击保存')
        # self.process.driver.switch_to.default_content()
        time.sleep(1.5)

    # 判断是否新增成功
    def add_success_text(self):
        el = self.process.find_success()
        if el:
            return el.text
        return ''

    # 创造不同账户名
    def add_diff_username(self):
        username = Faker(locale='zh-CN')
        return username.user_name()

    # 创造不同姓名
    def add_diff_name(self):
        name = Faker(locale='zh-CN')
        return name.name()