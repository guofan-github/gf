from CBT.ATM.action.action_zhsw_xjjh import Actionzhswxjjh
from CBT.ATM.common.logger import Log

class testxjjh():

    MODULE = '巡检计划'


    def __init__(self, report):
        self.action = Actionzhswxjjh()
        self.report = report
        self.logger = Log.get_logger()

    # 巡检计划-添加
    def test_xjjh_tianjia(self):
        case_title = '巡检计划-添加的测试'
        expected = '添加成功'
        resp = None

        try:
            resp = self.action.do_tianjia()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('巡检计划-添加的测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected},'
                                         f'但实际测试结果返回值是{resp.text}', '无')
                self.logger.info(f'巡检计划-添加的测试失败，期望结果是{expected}'
                                 f'而实际测试结果是{resp.text},'
                                 f'响应代码是{resp.status_code}'
                                 f'.\n请求url: {resp.request.url},'
                                 f' \n请求头: {resp.request.headers}'
                                 f' \n请求体: {resp.request.body}')
        except Exception as a:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(a)}。', '无')
            self.logger.error(f'巡检计划-添加的测试遇到意外错误，错误原因：{str(a)}。')
            if resp is not None:
                self.logger.info(f'巡检计划-添加的测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    # 查看
    def test_xjjh_chakan(self):
        case_title = '巡检计划-查看的测试'
        expected = 'OK'
        resp = None

        try:
            resp = self.action.do_chakan()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE,'接口测试',case_title,'成功','无','无')
                self.logger.info('巡检计划-查看的测试成功')
            else:
                self.report.write_report(self.MODULE,'接口测试',case_title,'失败'
                                         f'断言错误：期望请求返回值为{expected},'
                                         f'但实际测试结果返回值是{resp.text}','无')
                self.logger.info(f'巡检计划-查看的测试失败，期望结果是{expected}'
                                 f'而实际测试结果是{resp.text},响应代码是{resp.status_code}.\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as a:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(a)}。', '无')
            self.logger.error(f'巡检计划-查看的测试遇到意外错误，错误原因：{str(a)}。')
            if resp is not None:
                self.logger.info(f'巡检计划-查看的测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    # 查看-添加任务
    def test_xjjh_tianjiarenwu(self):
        case_title = '巡检计划-查看-添加任务的测试'
        expected = 'OK'
        resp = None

        try:
            resp = self.action.do_chakan()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE,'接口测试',case_title,'成功','无','无')
                self.logger.info('巡检计划-查看-添加任务的测试成功')
            else:
                self.report.write_report(self.MODULE,'接口测试',case_title,'失败'
                                         f'断言错误：期望请求返回值为{expected},'
                                         f'但实际测试结果返回值是{resp.text}','无')
                self.logger.info(f'巡检计划-查看-添加任务的测试失败，期望结果是{expected}'
                                 f'而实际测试结果是{resp.text},响应代码是{resp.status_code}.\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as a:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(a)}。', '无')
            self.logger.error(f'巡检计划-查看-添加任务的测试遇到意外错误，错误原因：{str(a)}。')
            if resp is not None:
                self.logger.info(f'巡检计划-查看-添加任务的测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')


    # 查看-添加任务-【添加】
    def test_xjjh_tianjiaer(self):
        case_title = '巡检计划-【添加】的测试'
        expected = '添加成功'
        resp = None

        try:
            resp = self.action.do_chakan_tianjiaer()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('巡检计划-【添加】的测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败'
                                                                          f'断言错误：期望请求返回值为{expected},'
                                                                          f'但实际测试结果返回值是{resp.text}', '无')
                self.logger.info(f'巡检计划-【添加】的测试失败，期望结果是{expected}'
                                 f'而实际测试结果是{resp.text},响应代码是{resp.status_code}.\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as a:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(a)}。', '无')
            self.logger.error(f'巡检计划-【添加】的测试遇到意外错误，错误原因：{str(a)}。')
            if resp is not None:
                self.logger.info(f'巡检计划-【添加】的测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')
