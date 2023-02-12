from common.common import Common
from common.report import Report
from test.test_login import Testloginui
from test.test_login_api import TestLoginApi


class ModuleLogin:

    def __init__(self, version):
        self.version = version


    def prepare(self):
        self.report = Report(self.version)
        self.ui_test = Testloginui(self.report)
        self.api_test = TestLoginApi(self.report)

    def finish(self):
        Common.close_browser()

    def main_test(self):
        self.prepare()
        self.ui_test.test_homepage()
        self.ui_test.test_login_cases()
        self.api_test.test_login_api()
        self.report.generate_report()
        # self.finish()

if __name__ == '__main__':
    ModuleLogin('0.01').main_test()