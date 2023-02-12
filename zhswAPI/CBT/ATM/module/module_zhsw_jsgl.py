from CBT.ATM.common.report import Report
from CBT.ATM.test.test_zhsw_jsgl import testjsgl

class Modulejsgl:
    def __init__(self,version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.test = testjsgl(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.test.test_jsgl_fpqx()
        self.test.test_jsgl_queding()
        self.finish()