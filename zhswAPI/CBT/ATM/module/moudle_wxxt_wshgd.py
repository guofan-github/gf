from CBT.ATM.common.report import Report
from CBT.ATM.test.test_wxxtwshgd_api import TsetWSHgdApi

class ModulewxxtWSHgd:
    def __init__(self,version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.wsh_test = TsetWSHgdApi(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.wsh_test.test_wshgd_jrym()
        self.wsh_test.test_wshgd_cx()
        self.wsh_test.test_wshgd_sh()
        self.wsh_test.test_wshgd_sc()
        self.finish()