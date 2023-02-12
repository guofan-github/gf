from CBT.ATM.common.report import Report
from CBT.ATM.test.test_wxxtypgd_api import TsetypgdApi

class Modulewxxtypgd:
    def __init__(self,version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.ypgd_test = TsetypgdApi(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.ypgd_test.test_ypgd_jrmk()
        self.ypgd_test.test_ypgd_cx()
        self.ypgd_test.test_ypgd_qsh()
        self.ypgd_test.test_ypgd_sc()
        self.finish()