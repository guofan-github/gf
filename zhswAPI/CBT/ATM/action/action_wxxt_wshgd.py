from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host

class ActionwshgdApi:

    def __init__(self):
        self.session = Common.get_session()

    def do_jrwshgd(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/user/repair',headers=hader)

    def do_wshgdcx(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        body = {"state":3,
                "source":"",
                "eventId":"",
                "reflectPeople":"",
                "phone":"15971456233",
                "reflectUnit":"",
                "reflectArea":"",
                "pappenArea":"",
                "pageIndex":1,
                "happenDate":"",
                "endDate":""}
        return self.session.post(f'http://{host}/water_bg/worker/list',headers=hader,json=body)

    def do_wshgdsh(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/repair/updateState?id=2&state=4',headers=hader)

    def do_wshgdsc(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/repair/delete?id=25',headers= hader)