from CBT.ATM.action.action_shlb import ActionShlb
from CBT.ATM.common.logger import Log


class TestShlb:
    MODULE = '采购审核模块'

    def __init__(self, report):
        self.action = ActionShlb()
        self.report = report
        self.logger = Log.get_logger()

    def test_getChecked_post(self):
        name = ''
        checkdate = ''
        case_title = '审核列表getChecked接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_getChecked_post(name, checkdate)
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('审核列表getChecked接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】审核列表getChecked接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'审核列表getChecked接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'审核列表getChecked接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_getUnchecked_post(self):
        name = ''
        no = ''
        case_title = '审核列表getUnchecked接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_getUnchecked_post(name, no)
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('审核列表getUnchecked接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】审核列表getUnchecked接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'审核列表getUnchecked接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'审核列表getUnchecked接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_check_post(self):
        id = "22"
        stockId = "1"
        description = "jack"
        useDate = "2022-06-20"
        buySum = "1"
        money = '23'
        buyDate = "2022-06-20"
        isChecked = "未审核"
        no = "bian2132"
        name = "变压器"
        buyman = "jack"
        case_title = '审核列表check接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_check_post(id, stockId, description, useDate, buySum, money, buyDate, isChecked, no,
                                             name, buyman)
            resp_json = resp.json()
            msg = resp_json['data']
            if resp.status_code == 200 and expected == msg["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('审核列表check接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】审核列表check接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'审核列表check接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'审核列表check接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_YSHQDchaxun_post(self):
        name = '变压器'
        checkdate = '2022-06-22'
        case_title = '审核列表已审核清单查询接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_YSHQDchaxun_post(name, checkdate)
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('审核列表已审核清单查询请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】审核列表已审核清单查询请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'审核列表已审核清单查询请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'审核列表已审核清单查询请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')



