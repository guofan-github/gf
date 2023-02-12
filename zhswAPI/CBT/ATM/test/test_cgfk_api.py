from CBT.ATM.action.action_cgfk import ActionCgfk
from CBT.ATM.common.logger import Log


class TestCgfk:
    MODULE = '采购审核模块'

    def __init__(self, report):
        self.action = ActionCgfk()
        self.report = report
        self.logger = Log.get_logger()

    def test_getbuybacks_post(self):
        pageIndex = '1'
        case_title = '采购反馈getbuybacks接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_getbuybacks_post(pageIndex)
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('采购反馈getbuybacks接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】采购反馈getbuybacks接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'采购反馈getbuybacks接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'采购反馈getbuybacks接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_CGFKchaxun_post(self):
        buyDate = '2021-03-02'
        buyman = '驱蚊器'
        pageIndex = '1'
        stockId = '2'
        case_title = '采购反馈查询接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_CGFKchaxun_post(buyDate, buyman, pageIndex, stockId)
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('采购反馈查询接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】采购反馈查询接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'采购反馈查询接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'采购反馈查询接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_CGFKtijiao_post(self):
        buycheckId = '66'
        dec = '2000'
        id = '51'
        realbuyCount = '2'
        realcost = '2000'
        realprice = '1000'
        status = '已完成'
        case_title = '采购反馈提交接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_CGFKtijiao_post(buycheckId, dec, id, realbuyCount, realcost, realprice, status)
            resp_json = resp.json()
            msg = resp_json['data']
            if resp.status_code == 200 and expected == msg["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('采购反馈提交接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】采购反馈提交接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'采购反馈提交接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'采购反馈提交接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')