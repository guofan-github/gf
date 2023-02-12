
from CBT.ATM.common.report import Report

from CBT.ATM.test.test_zhsw_jcss import testjcss


class Modulejcss:

    def __init__(self, version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.test = testjcss(self.report)

    def finish(self):
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.test.test_jcss_bengzhan()
        self.test.test_jcss_bianji()
        self.test.test_jcss_shenqingliebiao()
        self.test.test_jcss_xiangqing()
        self.test.test_jcss_xiugai()
        self.test.test_jcss_tianjia()
        self.test.test_jcss_shenqing2()
        self.finish()