from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host



class ActionBzsjxx:

    def __init__(self):
        self.session = Common.get_session()

    def do_getpumpdata_post(self, pageIndex):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {
            "pageIndex": pageIndex
        }
        return self.session.post(f'http://{host}/water_bg/gms/getpump', headers=head, json=body)