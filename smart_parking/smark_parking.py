
from common.report import Report
from module.module_login import ModuleLogin
from module.module_rights_management import ModuleRightsManagement
version = '0.07'
ModuleLogin(version).main_test()
ModuleRightsManagement(version).main_test()

# 发送邮件
report = Report(version)
att = report.compress_report()
report.send_report(att)
