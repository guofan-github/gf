from CBT.ATM.common.report import Report
from CBT.ATM.test.test_zhsw_xjsh import testxjsh

class Modulexjsh:
    def __init__(self,version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.test = testxjsh(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.test.test_xjsh_chaxun()
        self.test.test_xjsh_shenhe()

        self.finish()