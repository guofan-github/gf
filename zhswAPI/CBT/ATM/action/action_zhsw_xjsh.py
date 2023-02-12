from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host

# 巡检审核
class Actionzhswxjsh():

    def __init__(self):
        self.session = Common.get_session()

    # 查询
    def do_chaxun(self):
        head = {'Authorization': ActionLoginApi().get_login()}
        json = {"endDate": "",
                "startDate": "",
                "taskName": "",
                "taskNo": "PLAN-0016-20170817",
                "taskStatu": "",
                "taskType": ""}

        return self.session.post(f'http://{host}/water_bg/task/taskList?pageSize=5&pageIndex=1',json=json,headers=head)


    # 审核
    def do_shenhe(self):

        head = {'Authorization':ActionLoginApi().get_login()}

        json = {"ckAdvice": "",
                "ckResult": "审核通过",
                "taskId": 18}

        return self.session.post(f'http://{host}/water_bg/check/checkTask',json=json,headers=head)

