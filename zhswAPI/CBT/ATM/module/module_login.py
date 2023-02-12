from CBT.ATM.common.common import Common
from CBT.ATM.common.report import Report
from CBT.ATM.test.test_login_api import TsetLoginApi
from CBT.ATM.test.test_zhsw_jcss import testjcss


class ModuleLogin:

    def __init__(self, version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.api_test = TsetLoginApi(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.api_test.test_login()
        self.finish()

if __name__ == '__main__':
    ModuleLogin("0.08").main_test()