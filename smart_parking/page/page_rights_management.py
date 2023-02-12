from selenium.webdriver.common.by import By

from common.common import Common


class PageRightsManagement:

    def __init__(self):
        self.driver = Common.get_driver()

    # 权限管理导航栏定位
    def find_rights_management(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, '#app > section > section > aside > ul > div > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > li:nth-child(1) > div > span')

    # 账号管理导航栏定位
    def find_account_management(self):
        return Common.wait_element_presence(By.XPATH, '/html/body/div[1]/section/section/aside/ul/div/div[1]/div/li[1]/ul/li[1]/span')

    # 新增按钮定位
    def find_add_bwn(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, '#app > section > section > main > div:nth-child(3) > div.search > button.el-button.el-button--success.el-button--default.is-plain > span')

    # 账号输入框定位
    def find_account_input(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, '#app > section > section > main > div:nth-child(3) > form > div:nth-child(1) > div > div > input')

    # 密码输入框定位
    def find_password_input(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, '#app > section > section > main > div:nth-child(3) > form > div:nth-child(2) > div > div > input')

    # 确认密码输入框定位
    def find_password_reinput(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, '#app > section > section > main > div:nth-child(3) > form > div:nth-child(3) > div > div > input')

    # 电话输入框定位
    def find_tel_input(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, '#app > section > section > main > div:nth-child(3) > form > div:nth-child(4) > div > div > input')

    # 姓名输入框定位
    def find_name_input(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, '#app > section > section > main > div:nth-child(3) > form > div:nth-child(5) > div > div > input')

    # 角色下拉选择框定位
    def find_role_input(self):
        return Common.wait_element_presence(By.XPATH, '/html/body/div[1]/section/section/main/div[3]/form/div[6]/div/div/div/div[2]/input')

    # 角色选择定位
    def find_role(self):
        return Common.wait_element_presence(By.XPATH, '//*[@role="tooltip"]/div[1]/div/div[1]/ul/li[1]/span')

    # 收回下拉框
    def find_recover(self):
        return Common.wait_element_presence(By.XPATH, '/html/body/div[1]/section/header/div[2]/div[1]/i/svg/path')

    # 启用状态定位
    def find_enable(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, '#app > section > section > main > div:nth-child(3) > form > div:nth-child(7) > div > label:nth-child(1) > span.el-radio__input > span')

    # 保存按钮定位
    def find_save(self):
        return Common.wait_element_presence(By.CSS_SELECTOR, '#app > section > section > main > div:nth-child(3) > button.el-button.el-button--success.el-button--default > span')

    # 判断保存成功提示定位是否存在
    def find_success(self):
        el_path = '//div[@class="el-notification__content"]/p'

        return Common.wait_element_presence(By.XPATH, el_path)


