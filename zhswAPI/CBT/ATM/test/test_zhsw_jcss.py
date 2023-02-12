
from CBT.ATM.action.action_zhsw_jcss import Actionjcss
from CBT.ATM.common.logger import Log
from CBT.ATM.common.testdata import read_excel



class testjcss():


    MODULE = '基础设施页面'
    def __init__(self, report):
        self.action = Actionjcss()
        self.report = report
        self.logger = Log.get_logger()

    def test_jcss_bengzhan(self):
        case_title = '正确的泵站接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_bengzhan()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('基础设施泵站接口测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】基础设施泵站接口测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'登录请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')


    def test_jcss_xinzeng(self):
        case_title = '正确的新增接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_xinzeng()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('新增接口测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】新增测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'登录请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_jcss_xinzengqueding(self):
        case_title = '正确的新增确定接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_xinzengqueding()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('新增确定接口测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】新增确定测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'登录请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_jcss_bianji(self):
        case_title = '正确的编辑接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_bianji()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('编辑接口测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】编辑测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'登录请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_jcss_shenqingliebiao(self):
        case_title = '正确的申请列表接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_shenqingliebiao()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('申请列表接口测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】申请列表测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'登录请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_jcss_xiangqing(self):
        case_title = '正确的详情接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_xiangqing()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('详情接口测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】详情测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'登录请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')


    def test_jcss_xiugai(self):
        case_title = '正确的修改接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_xiugai()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('修改接口测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】修改测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'登录请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_jcss_tianjia(self):
        case_title = '正确的添加接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_tianjia()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('添加接口测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】添加测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'登录请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    def test_jcss_shenqing2(self):
        case_title = '正确的申请设备接口测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_shenqing2()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json["msg"]:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('申请设备接口测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】申请设备测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'登录请求遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'登录请求测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

