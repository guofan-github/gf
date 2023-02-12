from CBT.ATM.action.action_zhsw_jsgl import Actionzhswjsgl
from CBT.ATM.common.logger import Log


class testjsgl():
    MODULE = '角色管理'

    def __init__(self, report):
        self.action = Actionzhswjsgl()
        self.report = report
        self.logger = Log.get_logger()

    # 分配权限
    def test_jsgl_fpqx(self):
        case_title = '角色管理-分配权限的测试'
        expected = 'OK'
        resp = None
        try:
            resp = self.action.do_fenpeiquanxian()
            if resp.status_code == 200 and expected in resp.text:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('角色管理-分配权限的测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值为{expected}，'
                                         f'但实际测试结果返回值为{resp.text}', '无')
                self.logger.info(f'【接口测试】角色管理-分配权限的测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}')
        except Exception as e:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因：{str(e)}。', '无')
            self.logger.error(f'角色管理-分配权限的测试遇到意外错误，错误原因：{str(e)}。')
            if resp is not None:
                self.logger.info(f'角色管理-分配权限的测试失败. 期望结果是{expected}，'
                                 f'而实际测试结果是{resp.text}， 响应代码是{resp.status_code}。\n'
                                 f'请求url: {resp.request.url}, \n'
                                 f'请求头: {resp.request.headers} \n'
                                 f'请求体: {resp.request.body}.')

    # 确定
    def test_jsgl_queding(self):
        case_title = '角色管理-分配权限-确定'
        expected = 'OK'
        resp = None

        try:
            resp = self.action.do_queding()
            resp_json = resp.json()
            if resp.status_code == 200 and expected == resp_json['msg']:
                self.report.write_report(self.MODULE, '接口测试', case_title, '成功', '无', '无')
                self.logger.info('角色管理-分配权限-确定测试成功')
            else:
                self.report.write_report(self.MODULE, '接口测试', case_title, '失败',
                                         f'断言错误：期望请求返回值{expected}',
                                         f'但实际测试结果返回值{resp.text}', '无')
                self.logger.info(f'【接口测试】角色管理-分配权限-确定测试失败，期望结果是{expected}',
                                 f'而实际测试结果{resp.text}，响应代码是{resp.status_code}。\n'
                                 f'请求url:{resp.request.url},\n'
                                 f'请求头：{resp.request.headers},\n'
                                 f'请求体：{resp.request.body}')

        except Exception as a:
            self.report.write_report(self.MODULE, '接口测试', case_title, '错误',
                                     f'遇到意外错误，错误原因；{str(a)}.', '无')
            self.logger.error(f'角色管理-分配权限-确定遇到意外错误，错误原因；{str(a)}')

            if resp is not None:
                self.logger.info(f'角色管理-分配权限-确定测试失败，期望结果是{expected}'
                                 f'而实际测试结果是{resp.text},响应代码是{resp.status_code},\n'
                                 f'请求url:{resp.request.url}'
                                 f'请求头：{resp.request.headers}'
                                 f'请求体：{resp.request.body}')



