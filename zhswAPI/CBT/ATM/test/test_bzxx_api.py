from CBT.ATM.action.action_bzxx import ActionBzxx
from CBT.ATM.common.logger import Log


class TestBzxx:
    MODULE = 'G-M-S泵站模块'

    def __init__(self, report):
        self.action = ActionBzxx()
        self.report = report
        self.logger = Log.get_logger()

    def test_getusers_get(self):
        case_title = '泵站信息getusers接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_getusers_get()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('泵站信息getusers接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】泵站信息getusers接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'泵站信息getusers接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'泵站信息getusers接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')


    def test_getpump_post(self):
        pageIndex = '1'
        pumpname = '湖北一号站'
        pumptype = 'GD34'
        userId = '1'
        case_title = '泵站信息getpump接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_getpump_post(pageIndex, pumpname, pumptype, userId)
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('泵站信息getpump接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】泵站信息getpump接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'泵站信息getpump接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'泵站信息getpump接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_getallpump_get(self):
        case_title = '泵站信息getallpump接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_getallpump_get()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('泵站信息getallpump接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】泵站信息getallpump接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'泵站信息getallpump接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'泵站信息getallpump接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_updatepump_post(self):
        id = '22'
        pumpname = '湖北一号站'
        pumptype = 'GD34'
        gas = '5.55'
        tp = '5.56'
        intpower = '7.54'
        outpower = '6.34'
        temperature = '45'
        userId = '1'
        name = '余磊'
        pumpsize = '中'
        case_title = '泵站信息updatepump接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_updatepump_post(id, pumpname, pumptype, gas, tp, intpower, outpower, temperature,
                                                  userId, name,
                                                  pumpsize)
            resp_json = resp.json()
            msg = resp_json['data']
            if resp.status_code == 200 and expected == msg["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('泵站信息updatepump接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】泵站信息updatepump接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'泵站信息updatepump接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'泵站信息updatepump接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_addpump_post(self):
        pumpname = '1'
        pumptype = '1'
        gas = '1.00'
        tp = '1.00'
        intpower = '1.00'
        outpower = '6.34'
        temperature = '1.00'
        userId = '1'
        pumpsize = '大'
        case_title = '泵站信息addpump接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_addpump_post(gas, intpower, outpower, pumpname, pumpsize, pumptype, temperature, tp, userId)
            resp_json = resp.json()
            msg = resp_json['data']
            if resp.status_code == 200 and expected == msg["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('泵站信息addpump接口请求测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】泵站信息addpump接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'泵站信息addpump接口请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'泵站信息addpump接口请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')
