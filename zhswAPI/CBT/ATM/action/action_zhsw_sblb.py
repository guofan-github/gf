from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host


class Actionsblb():

    def __init__(self):
        self.session = Common.get_session()

    def do_xiugai(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        data = {"id":1,"no":"bian2132","name":"变压器","price":"9999","buyCount":"73"}
        return self.session.post(f'http://{host}/water_bg/basestock/updatebasestock', headers=head, json=data)

    def do_xiangqing(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/basestock/getBaseStock?id=1', headers=head)

    def do_shanchu(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }

        return self.session.get(f'http://{host}/water_bg/basestock/removebasestock?id=6', headers=head)

    def do_fenpeiliebiao(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/base/allBase', headers=head)

    def do_fenpei(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/device/disStockToBase?baseId=8&stockId=2&disNum=10', headers=head)

    def do_daipiliebiao(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/ask/getAskAll0', headers=head)

    def do_pifu(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/ask/getStock?stockId=1', headers=head)

    def do_pifuanniu(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/ask/Reply?id=46&okNum=5&explain=1', headers=head)

    def do_yipiliebiao(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/ask/getAskAll12', headers=head)

    def do_yipishanchu(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/ask/delBaseAsk?id=46', headers=head)
