from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host


class ActionLoginApi:

    def __init__(self):
        self.session = Common.get_session()

    def do_login(self, username, password):
        body = {"userName": username,
                "password": password}
        return self.session.post(f'http://{host}/water_bg/user/login', json=body)

    def get_login(self):
        user = 'admin'
        password = '123'
        resp = ActionLoginApi().do_login(user, password)
        v = resp.text.replace('"', "").replace('}', "").split(':')[-1]
        return v
