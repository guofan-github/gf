from CBT.ATM.action.action_bzsjxx import ActionBzsjxx
from CBT.ATM.common.logger import Log


class TestBzsjxx:
    MODULE = 'G-M-S泵站模块'

    def __init__(self, report):
        self.action = ActionBzsjxx()
        self.report = report
        self.logger = Log.get_logger()

    def test_getpumpdata_post(self):
        pageIndex = '1'
        case_title = '泵站数据信息getpumpdata接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_getpumpdata_post(pageIndex)
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('泵站数据信息getpumpdata接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】泵站数据信息getpumpdata接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'泵站数据信息getpumpdata接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'泵站数据信息getpumpdata接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')