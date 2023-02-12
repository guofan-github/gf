from CBT.ATM.common.report import Report
from CBT.ATM.test.test_zhsw_sblb import testsblb


class Modulesblb:

    def __init__(self, version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.test = testsblb(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.test.test_sblb_xiugai()
        self.test.test_sblb_xiangqing()
        self.test.test_sblb_shanchu()
        self.test.test_sblb_fenpeiliebiao()
        self.test.test_sblb_fenpei()
        self.test.test_sblb_daipiliebiao()
        self.test.test_sblb_pifu()
        self.test.test_sblb_pifuanniu()
        self.test.test_sblb_yipiliebiao()
        self.test.test_sblb_yipishanchu()
        self.finish()




