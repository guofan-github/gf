from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host


class ActionTjcgx:

    def __init__(self):
        self.session = Common.get_session()

    def do_tjcgx_get(self):
        head = {"Authorization": ActionLoginApi().get_login()}
        return self.session.get(f'http://{host}/water_bg/buy/getBaseStocks', headers=head)

    def do_tjcgx_post(self, buyman, stockId, useDate, buySum, buyDate, description, money, price):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {
            "buyman": buyman,
            "stockId": stockId,
            "useDate": useDate,
            "buySum": buySum,
            "buyDate": buyDate,
            "description": description,
            "money": money,
            "price": price
        }
        return self.session.post(f'http://{host}/water_bg/buy/addCheck', headers=head, json=body)
    # def do_test(self):
    #     head = {"Authorization": ActionLogin().get_authorization()}
    #     return self.session.get(f'http://{host}/water_bg/base/getBaseType?id=8', headers=head)
