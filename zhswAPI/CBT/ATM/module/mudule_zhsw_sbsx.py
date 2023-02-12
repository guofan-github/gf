from CBT.ATM.common.report import Report
from CBT.ATM.test.test_zhsw_sbsx import testsbsx


class Modulesbsx:

    def __init__(self, version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.test = testsbsx(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.test.test_sbsx_intoyemian()
        self.test.test_sbsx_jingtai()
        self.test.test_sbsx_dongtai()
        self.test.test_sbsx_xiugai()
        self.test.test_sbsx_tianjia()
        self.test.test_sbsx_shanchu()
        self.finish()