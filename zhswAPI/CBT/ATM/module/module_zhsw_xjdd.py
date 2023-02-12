from CBT.ATM.common.report import Report
from CBT.ATM.test.test_zhsw_xjdd import testxjdd

class Modulexjdd:
    def __init__(self,version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.test = testxjdd(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.test.test_xjdd_tianjia()
        self.test.test_xjdd_xiugai()
        self.finish()