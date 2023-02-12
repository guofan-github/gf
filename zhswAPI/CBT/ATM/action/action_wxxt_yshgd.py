from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host

class ActionywshgdApi:

    def __init__(self):
        self.session = Common.get_session()

    def do_jryshgd(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/user/repair',headers=hader)

    def do_yshgdcx(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        bady = {"state":4,
                "source":"",
                "eventId":"",
                "reflectPeople":"余磊阿松大",
                "phone":"",
                "reflectUnit":"森岭小镇",
                "reflectArea":"",
                "pappenArea":"",
                "pageIndex":1,
                "happenDate":"",
                "endDate":""}
        return self.session.post(f'http://{host}/water_bg/worker/list',json=bady,headers=hader)

    def do_yshgdsc(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/repair/delete?id=21',headers=hader)