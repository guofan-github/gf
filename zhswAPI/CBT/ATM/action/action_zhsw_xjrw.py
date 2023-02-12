from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host

# 巡检任务-查询
class Actionzhswxjrw():

    def __init__(self):
        self.session = Common.get_session()

    # 查询
    def do_chaxun(self):
        head = {'Authorization':ActionLoginApi().get_login()}
        json = {"endDate": "",
                "startDate": "",
                "taskName": "",
                "taskNo": "",
                "taskStatu": "",
                "taskType": "plan"}

        return self.session.post(f'http://{host}/water_bg/patrol/taskList?pageSize=5&pageIndex=1',headers=head,json=json)

