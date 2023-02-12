from action.action_login_api import ActionLoginApi
from common.logger import Log
from common.testdata import Read


class TestLoginApi:
    module = '登录模块'

    def __init__(self, report):
        self.action = ActionLoginApi()
        self.report = report
        self.logger = Log.get_logger()
        self.test_data = Read().get_data('登录测试数据', '登录测试')

    # 登录测试
    def login_api(self, user, pwd, code, msg):
        case_title = f'登录-{msg}接口测试'
        resp = None
        try:
            self.action.do_code()
            resp = self.action.do_login_api(user, pwd, code)
            if resp.json()["code"] == 200 and len(resp.json()["msg"]) > 50:
                self.report.write_report(self.module, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('正确的登录接口测试成功')
                print('登录-接口 成功')
            elif resp.json()['code'] == 500 and resp.json()["msg"] == msg:
                self.report.write_report(self.module, '接口测试', case_title, '成功', '无', '无')
                self.logger.info(f'{msg}登录接口测试成功')
            else:
                self.report.write_report(self.module, '接口测试', case_title, '失败',
                                         f'实际测试结果为{resp.text}', '无')
                self.logger.info(f'登录接口测试失败，实际测试结果为{resp.text}，'
                                 f'响应代码为{resp.status_code},'
                                 f'请求url为{resp.request.url},'
                                 f'请求头为{resp.request.headers},'
                                 f'请求体为{resp.request.body}。')
        except Exception as e:
            self.report.write_report(self.module, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'登录接口测试错误，'
                                 f'实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url：{resp.request.url}，\n'
                                 f'请求头：{resp.request.headers},\n'
                                 f'请求体：{resp.request.body}。')

    def test_login_api(self):
        for case in self.test_data:
            self.login_api(*case)


if __name__ == '__main__':
    TestLoginApi('0').test_login_api()
