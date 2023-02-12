import six

from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host


class ActionsbwxApi:

    def __init__(self):
        self.session = Common.get_session()

    def do_jrsbwx(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        body = {"createDate":"","endDate":"","pageIndex":"1","pageSize":"5","childStatus":"","baseName":""}
        return self.session.post(f'http://{host}/water_bg/baseRepair/List',headers=hader,json=body)

    def do_sbwxcx(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        body = {"createDate":"","endDate":"","pageIndex":"1","pageSize":"5","childStatus":"已报修","baseName":""}
        return self.session.post(f'http://{host}/water_bg/baseRepair/List',json=body,headers=hader)

    def do_sbwx_wcjx(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/baseRepair/updateStatus?deviceId=17',headers=hader)

    def do_sbwx_sc(self):
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/baseRepair/delete?id=18',headers=hader)