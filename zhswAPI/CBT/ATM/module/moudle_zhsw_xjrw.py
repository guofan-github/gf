from CBT.ATM.common.report import Report
from CBT.ATM.test.test_zhsw_xjrw import testxjrw

class Modulexjrw:
    def __init__(self,version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.test = testxjrw(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.test.test_xjrw_chaxun()
        self.finish()