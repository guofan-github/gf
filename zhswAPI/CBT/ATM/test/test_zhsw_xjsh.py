from CBT.ATM.action.action_zhsw_xjsh import Actionzhswxjsh
from CBT.ATM.common.logger import Log

class testxjsh():

    MODULE = '巡检审核'

    def __init__(self, report):
        self.action = Actionzhswxjsh()
        self.report = report
        self.logger = Log.get_logger()

    # 查询
    def test_xjsh_chaxun(self):
        case_title = '巡检审核-查询的测试'
        expected = 'OK'
        resp = None

        try:
            resp = self.action.do_chaxun()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE,'接口测试',case_title,'成功','无','无')
                self.logger.info('巡检审核-查询的测试成功')
            else:
                self.report.write_report(self.MODULE,'接口测试',case_title,'失败'
                                         f'断言错误：期望请求返回值为{expected},'
                                         f'但实际测试结果返回值是{resp.text}','无')
                self.logger.info(f'巡检审核-查询的测试失败，期望结果是{expected}'
                                 f'而实际测试结果是{resp.text},响应代码是{resp.status_code}.\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as a:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(a)}。', '无')
            self.logger.error(f'巡检审核-查询的测试遇到意外错误，错误原因：{str(a)}。')
            if resp is not None:
                self.logger.info(f'巡检审核-查询的测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    # 审核
    def test_xjsh_shenhe(self):
        case_title = '巡检计划-审核的测试'
        expected = '审核成功'
        resp = None

        try:
            resp = self.action.do_shenhe()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE,'接口测试',case_title,'成功','无','无')
                self.logger.info('巡检计划-审核的测试成功')
            else:
                self.report.write_report(self.MODULE,'接口测试',case_title,'失败'
                                         f'断言错误：期望请求返回值为{expected},'
                                         f'但实际测试结果返回值是{resp.text}','无')
                self.logger.info(f'巡检计划-审核的测试失败，期望结果是{expected}'
                                 f'而实际测试结果是{resp.text},响应代码是{resp.status_code}.\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as a:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(a)}。', '无')
            self.logger.error(f'巡检计划-审核的测试遇到意外错误，错误原因：{str(a)}。')
            if resp is not None:
                self.logger.info(f'巡检计划-审核的测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

