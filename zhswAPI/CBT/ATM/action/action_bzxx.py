from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host



class ActionBzxx:

    def __init__(self):
        self.session = Common.get_session()

    def do_getusers_get(self):
        head = {"Authorization": ActionLoginApi().get_login()}
        return self.session.get(f'http://{host}/water_bg/gms/getusers', headers=head)

    def do_getpump_post(self, pageIndex, pumpname, pumptype, userId):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {
            "pageIndex": pageIndex,
            "pumpname": pumpname,
            "pumptype": pumptype,
            "userId": userId
        }
        return self.session.post(f'http://{host}/water_bg/gms/getpump', headers=head, json=body)

    def do_getallpump_get(self):
        head = {"Authorization": ActionLoginApi().get_login()}
        return self.session.get(f'http://{host}/water_bg/gms/getallpump', headers=head)

    def do_updatepump_post(self, id, pumpname, pumptype, gas, tp, intpower, outpower, temperature, userId, name,
                           pumpsize):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {"id": id, "pumpname": pumpname, "pumptype": pumptype, "gas": gas, "tp": tp, "intpower": intpower,
                "outpower": outpower, "temperature": temperature, "userId": userId, "name": name, "pumpsize": pumpsize}
        return self.session.post(f'http://{host}/water_bg/gms/updatepump', headers=head, json=body)

    def do_addpump_post(self, gas, intpower, outpower, pumpname, pumpsize, pumptype, temperature, tp, userId):
        head = {"Authorization": ActionLoginApi().get_login()}
        body = {
            "gas": gas,
            "intpower": intpower,
            "outpower": outpower,
            "pumpname": pumpname,
            "pumpsize": pumpsize,
            "pumptype": pumptype,
            "temperature": temperature,
            "tp": tp,
            "userId": userId
        }
        return self.session.post(f'http://{host}/water_bg/gms/addpump', headers=head, json=body)


