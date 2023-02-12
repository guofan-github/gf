from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.logger import Log
from CBT.ATM.common.testdata import read_excel
from CBT.ATM.data.ddt import data


class TsetLoginApi:
    MODULE = '登录接口模块'
    # aa = read_excel().get_data("jcss修改", '修改')
    def __init__(self, report):
        self.action = ActionLoginApi()
        self.report = report
        self.logger = Log.get_logger()

    @data(read_excel().get_data("jcss修改", '修改'))
    def test_login(self, user, password, case_title, expected):
        # user = 'admin'
        # password = '123'
        # case_title = '正确的账户登录接口测试'
        # expected = '郭凡'
        resp = None
        try:
            resp = self.action.do_login(user, password)
            if resp.status_code == 200 and  expected in resp.text:
                self.report.write_report(self.MODULE,'接口测试', case_title, '成功', '无', '无')
                self.logger.info('登录请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】登录请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'登录请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

