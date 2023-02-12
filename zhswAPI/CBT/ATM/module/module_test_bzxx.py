from CBT.ATM.common.report import Report
from CBT.ATM.test.test_bzxx_api import TestBzxx


class ModuleBzxx:

    def __init__(self, version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.api_bzxx = TestBzxx(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.api_bzxx.test_getusers_get()
        self.api_bzxx.test_getpump_post()
        self.api_bzxx.test_getallpump_get()
        self.api_bzxx.test_updatepump_post()
        self.api_bzxx.test_addpump_post()
        self.finish()