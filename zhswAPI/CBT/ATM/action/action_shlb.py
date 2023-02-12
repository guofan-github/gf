from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host



class ActionShlb:

    def __init__(self):
        self.session = Common.get_session()

    def do_getChecked_post(self, name, checkdate):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {
            "name": name,
            "checkDate": checkdate
        }
        return self.session.post(f'http://{host}/water_bg/buy/getChecked', headers=head, json=body)

    def do_getUnchecked_post(self, name, no):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {
            "name": name,
            "no": no
        }
        return self.session.post(f'http://{host}/water_bg/buy/getUnchecked', headers=head, json=body)

    def do_check_post(self, id, stockId, description, useDate, buySum, money, buyDate, isChecked, no, name, buyman):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {
            'id': id,
            "stockId": stockId,
            "description": description,
            "useDate": useDate,
            "buySum": buySum,
            "money": money,
            "buyDate": buyDate,
            "isChecked": isChecked,
            "no": no,
            "name": name,
            "buyman": buyman,
        }
        return self.session.post(f'http://{host}/water_bg/buy/check', headers=head, json=body)

    def do_YSHQDchaxun_post(self, name, checkdate):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {
            "name": name,
            "checkDate": checkdate
        }
        return self.session.post(f'http://{host}/water_bg/buy/getChecked', headers=head, json=body)


if __name__ == '__main__':
    ActionShlb().do_check_post()