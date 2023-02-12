from CBT.ATM.common.report import Report
from CBT.ATM.test.test_wxxtyshgd_api import TsetyshgdApi

class Modulewxxtyshgd:
    def __init__(self,version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.yshgd_test = TsetyshgdApi(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.yshgd_test.test_yshgd_jrmk()
        self.yshgd_test.test_yshgd_cx()
        self.yshgd_test.test_yshgd_sc()
        self.finish()