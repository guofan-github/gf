from action.action_rights_management_api import ActionRightsManagementapi
from common.logger import Log
from common.testdata import Read


class TestRightsManagementApi:
    module = '账号管理'

    def __init__(self, report):
        self.action = ActionRightsManagementapi()
        self.report = report
        self.logger = Log.get_logger()
        self.test_data = Read().get_data('新增账户', 'Sheet1')

    # 新增账户测试
    def add_account_api(self, account, pwd, repwd, tel, name, role, status, msg):
        case_title = '新增账号管理接口测试'
        resp = None
        try:
            resp = self.action.do_add_account(account, pwd, repwd, tel, name, role, status)
            if resp.json()['code'] == 200 and resp.json()["msg"] == msg:
                self.report.write_report(self.module, '接口测试', case_title, '成功', '无', '无')
                self.logger.info(f'新增账户-{msg}接口测试成功')
                print('新增账户-接口 测试成功')
            elif resp.json()['code'] == 500 and resp.json()["msg"] == msg:
                self.report.write_report(self.module, '接口测试', case_title, '成功', '无', '无')
                self.logger.info(f'新增账户-{msg}接口测试成功')
            else:
                self.report.write_report(self.module, '接口测试', case_title, '失败',
                                         f'实际测试结果为{resp.text}', '无')
                self.logger.info(f'{case_title}失败，实际测试结果为{resp.text}，'
                                 f'响应代码为{resp.status_code},'
                                 f'请求url为{resp.request.url},'
                                 f'请求头为{resp.request.headers},'
                                 f'请求体为{resp.request.body}。')
        except Exception as e:
            self.report.write_report(self.module, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'{case_title}错误，'
                                 f'实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url：{resp.request.url}，\n'
                                 f'请求头：{resp.request.headers},\n'
                                 f'请求体：{resp.request.body}。')

    def test_add_account_api_case(self):
        for case in self.test_data:
            self.add_account_api(*case)
