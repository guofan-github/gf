from CBT.ATM.common.report import Report
from CBT.ATM.test.test_zhsw_xjjh import testxjjh

class Modulexjjh:
    def __init__(self,version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.test = testxjjh(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.test.test_xjjh_tianjia()
        self.test.test_xjjh_chakan()
        self.test.test_xjjh_tianjiarenwu()
        self.test.test_xjjh_tianjiaer()
        self.finish()