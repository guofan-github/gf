from CBT.ATM.common.report import Report
from CBT.ATM.test.test_shlb_api import TestShlb


class ModuleShlb:

    def __init__(self, version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.api_shlb = TestShlb(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.api_shlb.test_getChecked_post()
        self.api_shlb.test_getUnchecked_post()
        self.api_shlb.test_check_post()
        self.api_shlb.test_YSHQDchaxun_post()
        self.finish()