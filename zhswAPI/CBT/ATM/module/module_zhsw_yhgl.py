from CBT.ATM.common.report import Report
from CBT.ATM.test.test_zhsw_yhgl import testyhgl

class Moduleyhgl:
    def __init__(self,version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.test = testyhgl(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.test.test_yhgl_chaxun()
        self.test.test_yhgl_xiugai()
        self.finish()