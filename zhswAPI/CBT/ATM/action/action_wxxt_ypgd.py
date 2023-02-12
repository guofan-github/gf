from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host


class ActionypgdApi:

    def __init__(self):
        self.session = Common.get_session()

    def do_jrypgd(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/user/repair',headers= hader)

    def do_ypgdcx(self):
        body = {"state":2,
                "source":"",
                "eventId":"",
                "reflectPeople":"",
                "phone":"",
                "reflectUnit":"计划生育小组",
                "reflectArea":"","pappenArea":"",
                "pageIndex":1,
                "happenDate":"",
                "endDate":""}
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.post(f'http://{host}/water_bg/worker/list',headers=hader,json=body)

    def do_ypgdqsh(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/repair/updateState?id=37&state=3',headers=hader)

    def do_ypgdsc(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/repair/delete?id=43',headers=hader)