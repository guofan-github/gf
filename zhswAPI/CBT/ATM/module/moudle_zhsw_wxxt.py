from CBT.ATM.common.report import Report
from CBT.ATM.test.test_wxxt_api import TsetwpgdApi

class Modulewxxtwpgd:
    def __init__(self,version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.y_test = TsetwpgdApi(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.y_test.test_wpgd_tjgd()
        self.y_test.test_wpgd_cz()
        self.y_test.test_wpgd_jrmk()
        self.y_test.test_wpgd_cx()
        self.y_test.test_wpgd_xg()
        self.y_test.test_wpgd_sc()
        self.y_test.test_wpgd_fy()
        self.finish()

