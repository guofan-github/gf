import time

from action.action_login import ActionLoginUI
from common.common import Common
from common.logger import Log
from common.testdata import Read
from procrss.process_login import ProcessLogin


class Testloginui:

    def __init__(self, report):
        self.action = ActionLoginUI()
        self.login = ProcessLogin()
        self.report = report
        self.module = '登录模块'
        self.logger = Log.get_logger()
        self.test_data = Read().get_data('登录测试数据', '登录测试')

    # 测试首页访问
    def test_homepage(self):
        case_title = "访问首页测试"
        expected = True
        try:
            self.action.do_homepage()
            if self.login.check_username() == expected:
                self.report.write_report(self.module, 'UI', case_title, '成功', '无', '无')
                self.logger.info('访问首页测试成功')
                print("访问首页成功")
            else:
                screenshot = self.report.capture_screenshot(Common.get_driver())
                self.report.write_report(self.module, 'UI', case_title, '失败',
                                         '断言失败:期望不存在', screenshot)
                print("访问首页失败")
                self.logger.info(f'访问首页测试失败')
        except Exception as e:
            screenshot = self.report.capture_screenshot(Common.get_driver())
            self.report.write_report(self.module, 'UI', case_title, '错误',
                                     f'发生意外错误,错误原因：{str(e)}', screenshot)
            print(f'访问首页测试出现错误：{str(e)}')
            self.logger.info(f'发生意外错误，错误原因：{str(e)}')

    # 登录测试

    def test_login(self, username, pwd, code, msg):
        case_title = f'{msg}登录测试'
        expected = msg
        try:
            self.action.do_login(username, pwd, code)
            if expected == '登录成功':
                if self.login.login_text() == '首页':
                    self.report.write_report(self.module, 'UI', case_title, '成功', '无', '无')
                    print('登录成功')
                    self.logger.info('登录测试成功')

                else:
                    screenshot = self.report.capture_screenshot(Common.get_driver())
                    self.report.write_report(self.module, 'UI', case_title, '失败',
                                             f'断言失败:{expected}!={self.login.login_text()}', screenshot)
                    print('登录失败')
                    self.logger.info(f'登录测试失败，{expected}不符合期望值')
            elif expected != '登录成功':
                if self.login.login_error_text() == expected:
                    self.report.write_report(self.module, 'UI', case_title, '成功', '无', '无')
                    print(f'{expected}登录测试成功')
                    self.logger.info(f'{expected}登录测试成功')
                    self.login.click_login_error_btn()

                else:
                    screenshot = self.report.capture_screenshot(Common.get_driver())
                    self.report.write_report(self.module, 'UI', case_title, '失败',
                                             f'断言失败:{expected}!={self.login.login_error_text()}', screenshot)
                    print(f'{expected}登录失败')
                    self.logger.info(f'{expected}登录测试失败，{expected}不符合期望值')

                    self.login.click_login_error_btn()
        except Exception as e:
            screenshot = self.report.capture_screenshot(Common.get_driver())
            self.report.write_report(self.module, 'UI', case_title, '错误',
                                     f'发生意外错误,错误原因：{str(e)}', screenshot)
            print(f'登录测试出现问题：{str(e)}')
            self.logger.info(f'发生意外错误，错误原因：{str(e)}')

    def test_login_cases(self):
        for case in self.test_data:
            self.test_login(*case)
