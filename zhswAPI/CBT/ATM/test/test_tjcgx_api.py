import time

from CBT.ATM.action.action_tjcgx import ActionTjcgx
from CBT.ATM.common.logger import Log


class TestTjcgx:
    MODULE = '采购审核模块'

    def __init__(self, report):
        self.action = ActionTjcgx()
        self.report = report
        self.logger = Log.get_logger()

    def test_tjcgx_get(self):
        case_title = '添加采购项页面接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_tjcgx_get()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('添加采购项页面请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】添加采购项页面请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'添加采购项页面请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'添加采购项页面请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_tjcgx_post(self):
        buyman = "jack"
        stockId = "1"
        useDate = "2022-06-21"
        buySum = "1"
        buyDate = "2022-06-21"
        description = "jack"
        money = "23"
        price = "23"
        case_title = '添加采购项添加接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_tjcgx_post(buyman, stockId, useDate, buySum, buyDate, description, money, price)
            resp_json = resp.json()
            msg = resp_json['data']
            if resp.status_code == 200 and expected == msg["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('添加采购项添加请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】添加采购项添加请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'添加采购项添加请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'添加采购项添加请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')
    # def test_test(self):
    #     case_title = '正确的账户登录接口测试'
    #     expected = 'OK'
    #     resp = None
    #     try:
    #         resp = self.action.do_test()
    #         resp_json = resp.json()
    #         if resp.status_code == 200 and expected == resp_json["msg"]:
    #             self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
    #             self.logger.info('请求测试成功')
    #         else:
    #             self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
    #                                      f'断言错误：期望请求返回值为{expected}，'
    #                                      f'但实际测试结果返回值为{resp.text}', '无')
    #             self.logger.info(f'【接口测试】请求测试失败. 期望结果是{expected}，'
    #                              f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
    #                              f'请求url: {resp.request.url}, \n'
    #                              f'请求头: {resp.request.headers} \n'
    #                              f'请求体: {resp.request.body}')
    #     except Exception as e:
    #         self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
    #                                  f'遇到意外错误，错误原因：{str(e)}。', '无')
    #         self.logger.error(f'请求遇到意外错误，错误原因：{str(e)}。')
    #         if resp is not None:
    #             self.logger.info(f'请求测试失败. 期望结果是{expected}，'
    #                              f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
    #                              f'请求url: {resp.request.url}, \n'
    #                              f'请求头: {resp.request.headers} \n'
    #                              f'请求体: {resp.request.body}.')
