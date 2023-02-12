from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host

# 系统管理-角色管理
class Actionzhswjsgl():

    def __init__(self):
        self.session = Common.get_session()

    # 角色管理
    def do_jueseguanli(self):
        head = {'Authorization':ActionLoginApi().get_login()}
        return self.session.get(f'http://{host}/water_bg/role/list',headers=head)


    # 分配权限
    def do_fenpeiquanxian(self):
        head = {'Authorization':ActionLoginApi().get_login()}
        return self.session.get(f'http://{host}/water_bg/roleperm/tree?id=1', headers=head)

    # 确定
    def do_queding(self):
        head = {'Authorization':ActionLoginApi().get_login()}
        return self.session.get(f'http://{host}/water_bg/role/prem/assignRight?keys=1,3,4,5,6,7,8,9,10,11,12,48,49,13,14,15,45,46,50,51,52,53,54,55,56,57,58,59&roleId=1',headers=head)

