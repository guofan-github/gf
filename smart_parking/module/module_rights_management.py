from common.common import Common
from common.report import Report
from test.test_rightsmanagement import TestRightsManagement
from test.test_rightsmanagement_api import TestRightsManagementApi


class ModuleRightsManagement:

    def __init__(self, version):
        self.version = version

    def prepare(self):
        self.report = Report(self.version)
        self.rights = TestRightsManagement(self.report)
        self.testapi = TestRightsManagementApi(self.report)

    def finish(self):
        Common.close_browser()
        self.report.generate_report()

    def main_test(self):
        self.prepare()
        self.rights.test_add_account()
        self.testapi.test_add_account_api_case()
        self.finish()

