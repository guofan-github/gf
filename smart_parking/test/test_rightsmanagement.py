from action.action_rights_management import ActionRightsManagement
from common.common import Common
from common.logger import Log
from common.testdata import Read
from procrss.process_rights_management import ProcessRightsManagement


class TestRightsManagement:

    def __init__(self, report):
        self.RM = ActionRightsManagement()
        self.addsu = ProcessRightsManagement()
        self.report = report
        self.module = '权限管理'
        self.logger = Log.get_logger()


    # 新增账户测试
    def test_add_account(self):
        case_title = '新增账户测试'
        account = self.addsu.add_diff_username()
        pwd = 'vvv333'
        repwd = 'vvv333'
        tel = '13333333333'
        name = self.addsu.add_diff_name()
        expected = '账号创建成功'
        try:
            self.RM.do_add_account(account, pwd, repwd, tel, name)
            if self.addsu.add_success_text() == expected:
                self.report.write_report(self.module, 'UI', case_title, '成功', '无', '无')
                print("新增账户成功")
                self.logger.info('新增账户测试成功')
            else:
                screenshot = self.report.capture_screenshot(Common.get_driver())
                self.report.write_report(self.module, 'UI', case_title, '失败',
                                         f'断言失败:{expected}!={self.addsu.add_success_text()}', screenshot)
                print("新增账户失败")
                self.logger.info(f'新增账户测试失败，断言不符合期望值')
        except Exception as e:
            screenshot = self.report.capture_screenshot(Common.get_driver())
            self.report.write_report(self.module, 'UI', case_title, '错误',
                                     f'发生意外错误,错误原因：{str(e)}', screenshot)
            print(f'新增账户出现错误：str{e}')
            self.logger.info(f'发生意外错误，错误原因：{str(e)}')


