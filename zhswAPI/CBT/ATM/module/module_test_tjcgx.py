from CBT.ATM.common.report import Report
from CBT.ATM.test.test_tjcgx_api import TestTjcgx


class ModuleTjcgx:

    def __init__(self, version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.api_tjcgx = TestTjcgx(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.api_tjcgx.test_tjcgx_get()
        self.api_tjcgx.test_tjcgx_post()
        self.finish()