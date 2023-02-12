from CBT.ATM.common.report import Report
from CBT.ATM.test.test_cgfk_api import TestCgfk


class ModuleCgfk:

    def __init__(self, version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.api_cgfk = TestCgfk(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.api_cgfk.test_getbuybacks_post()
        self.api_cgfk.test_CGFKchaxun_post()
        self.api_cgfk.test_CGFKtijiao_post()
        self.finish()