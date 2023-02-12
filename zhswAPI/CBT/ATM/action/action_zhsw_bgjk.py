from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host


class Actionbgjk():

    def __init__(self):
        self.session = Common.get_session()

    def do_boom(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/boom/getAll', headers=head)

    def do_jiankong(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/boom/waterLevel', headers=head)

    




