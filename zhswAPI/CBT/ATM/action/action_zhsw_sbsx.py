from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host


class Actionsbsx():

    def __init__(self):
        self.session = Common.get_session()

    def do_intoyemian(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/device/getAllMenu', headers=head)

    def do_jingtai(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/device/getStaticAll?id=1', headers=head)

    def do_dongtai(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/device/getSurveyAll?id=1', headers=head)

    def do_xiugai(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        data = {"id":1,"describe":"sb","unit":"sb","stockId":1}
        return self.session.post(f'http://{host}/water_bg/device/updateStatic', json=data, headers=head)

    def do_tianjia(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        data = {"id":"","describe":"ssss","unit":"sb","stockId":"1"}
        return self.session.post(f'http://{host}/water_bg/device/addStatic',json=data, headers=head)

    def do_shanchu(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/device/delStatic?id=3', headers=head)




