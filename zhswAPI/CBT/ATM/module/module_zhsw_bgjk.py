from CBT.ATM.common.report import Report
from CBT.ATM.test.test_zhsw_bgjk import testbgjk


class Modulebgjk:

    def __init__(self, version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.test = testbgjk(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.test.test_bgjk_boom()
        self.test.test_bgjk_jiankong()
        self.finish()



