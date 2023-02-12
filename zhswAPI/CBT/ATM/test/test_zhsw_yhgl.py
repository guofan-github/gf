from CBT.ATM.action.action_zhsw_yhgl import Actionzhswyhgl
from CBT.ATM.common.logger import Log

class testyhgl():

    MODULE = '用户管理'


    def __init__(self, report):
        self.action = Actionzhswyhgl()
        self.report = report
        self.logger = Log.get_logger()

    # 查询
    def test_yhgl_chaxun(self):
        case_title = '用户管理-查询的测试'
        expected = 'OK'
        resp = None

        try:
            resp = self.action.do_chaxun()
            resp_json = resp.json()
            if resp.status_code == 200 and expected ==resp_json['msg']:
                self.report.write_report(self.MODULE,'接口测试',case_title,'成功','无','无')
                self.logger.info('用户管理-查询的测试成功')
            else:
                self.report.write_report(self.MODULE,'接口测试',case_title,'失败'
                                         f'断言错误：期望请求返回值为{expected},'
                                         f'但实际测试结果返回值是{resp.text}','无')
                self.logger.info(f'【接口测试】用户管理-查询的测试失败，期望结果是{expected}'
                                 f'而实际测试结果是{resp.text},响应代码是{resp.status_code}.\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as a:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(a)}。', '无')
            self.logger.error(f'用户管理-查询的测试遇到意外错误，错误原因：{str(a)}。')
            if resp is not None:
                self.logger.info(f'用户管理-查询的测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    # 修改
    def test_yhgl_xiugai(self):
        case_title = '用户管理-修改的测试'
        expected = 'OK'
        resp = None

        try:
            resp = self.action.do_xiugai()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE,'接口测试',case_title,'成功','无','无')
                self.logger.info('用户管理-修改的测试成功')
            else:
                self.report.write_report(self.MODULE,'接口测试',case_title,'失败',
                                         f'断言错误：期望请求返回值{expected}'
                                         f'实际的测试结果是{resp.text}','无')
                self.logger.info(f'【接口测试】用户管理-修改的测试失败，期望结果{expected}'
                                 f'而实际的测试结果{resp.text},响应代码{resp.status_code}'
                                 f'url的请求：{resp.request.url}'
                                 f'请求头；{resp.request.headers}'
                                 f'请求体：{resp.request.body}')
        except Exception as a:
            self.report.write_report(self.MODULE,'接口测试',case_title,'错误',
                                     f'遇到意外错误，错误的原因{str(a)}','无')
            self.logger.error(f'用户管理-修改的测试遇到意外错误，错误原因{str(a)}')

            if resp is not None:
                self.logger.info(f'用户管理-修改的测试失败，期望结果是{expected}'
                                 f'而实际测试结果是{resp.text},响应代码是{resp.status_code},\n'
                                 f'请求url:{resp.request.url}'
                                 f'请求头：{resp.request.headers}'
                                 f'请求体：{resp.request.body}')







