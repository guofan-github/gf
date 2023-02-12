from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host



class ActionCgfk:

    def __init__(self):
        self.session = Common.get_session()

    def do_getbuybacks_post(self, pageIndex):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {
            "pageIndex": pageIndex
        }
        return self.session.post(f'http://{host}/water_bg/buyback/getbuybacks', headers=head, json=body)

    def do_CGFKchaxun_post(self, buyDate, buyman, pageIndex, stockId):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {
            "buyDate": buyDate,
            "buyman": buyman,
            "pageIndex": pageIndex,
            "stockId": stockId
        }
        return self.session.post(f'http://{host}/water_bg/buyback/getbuybacks', headers=head, json=body)

    def do_CGFKtijiao_post(self, buycheckId, dec, id, realbuyCount, realcost, realprice, status):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {
            "buycheckId": buycheckId,
            "dec": dec,
            "id": id,
            "realbuyCount": realbuyCount,
            "realcost": realcost,
            "realprice": realprice,
            "status": status
        }
        return self.session.post(f'http://{host}/water_bg/buyback/update', headers=head, json=body)