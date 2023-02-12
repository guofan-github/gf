from CBT.ATM.common.report import Report
from CBT.ATM.test.test_bzsjxx_api import TestBzsjxx


class ModuleBzsjxx:

    def __init__(self, version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.api_bzsjxx = TestBzsjxx(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.api_bzsjxx.test_getpumpdata_post()
        self.finish()