from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host

# 系统管理-用户管理
class Actionzhswyhgl():

    def __init__(self):
        self.session = Common.get_session()


    # 用户管理
    def do_yonghuguanli(self):
        head = {'Authorization': ActionLoginApi().get_login()}
        return self.session.get(f'http://{host}/water_bg/role/list',headers=head)
    # 查询
    def do_chaxun(self):

        head = {'Authorization':ActionLoginApi().get_login()}

        params = {"pageIndex": 1,
                "name": "郭凡",
                "roleId":""}

        return self.session.get(f'http://{host}/water_bg/user/getAll?pageIndex=1&name=%E9%83%AD%E5%87%A1&roleId=',params=params,headers=head)

    # 修改
    def do_xiugai(self):
        head = {'Authorization': ActionLoginApi().get_login()}

        data = {"id": 1,
                "name": "郭凡",
                "password": "225",
                "phone": "13353430752",
                "roleId": 4,
                "userName":""}

        return self.session.post(f'http://{host}/water_bg/user/updateUser',json=data,headers=head)



