from CBT.ATM.common.logger import Log
from CBT.ATM.action.action_wxxt_wshgd import ActionwshgdApi



class TsetWSHgdApi:
    MODULE = '维修系统已派工单接口模块'

    def __init__(self, report):
        self.action = ActionwshgdApi()
        self.report = report
        self.logger = Log.get_logger()

    def test_wshgd_jrym(self):
        case_title = '进入未审核工单测试'
        expected = "OK"
        resp = None
        try:
            resp = self.action.do_jrwshgd()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('进入未审核工单模块正常')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】进入未审核工单请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'进入未审核工单请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'进入未审核工单请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_wshgd_cx(self):
        case_title = '未审核工单查询测试'
        expected = "ok"
        resp = None
        try:
            resp = self.action.do_wshgdcx()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('未审核工单查询模块正常')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】未审核工单查询请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'未审核工单查询请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'未审核工单查询请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_wshgd_sh(self):
        case_title = '未审核工单审核测试'
        expected = "OK"
        resp = None
        try:
            resp = self.action.do_wshgdsh()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('未审核工单审核模块正常')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】未审核工单审核请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'未审核工单审核请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'未审核工单审核请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_wshgd_sc(self):
        case_title = '未审核工单删除'
        expected = "OK"
        resp = None
        try:
            resp = self.action.do_wshgdsc()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('未审核工单删除正常')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】进入已派请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'未审核工单删除请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'未审核工单删除请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')