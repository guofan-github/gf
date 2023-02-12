from CBT.ATM.common.report import Report
from CBT.ATM.test.test_wxxtsbwx_api import TsetsbwxApi

class Modulewxxtsbwx:
    def __init__(self,version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.sbwx_test = TsetsbwxApi(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.sbwx_test.test_sbwx_jrmk()
        self.sbwx_test.test_sbwx_cx()
        self.sbwx_test.test_sbwx_wcwx()
        self.sbwx_test.test_sbwx_sc()
        self.finish()