from common.common import Common


class ActionRightsManagementapi:

    def __init__(self):
        self.session = Common.get_session()

    # 新增账户
    def do_add_account(self, account, pwd, repwd, tel, name, role, state):

        data = {"id":"-1","accountName":account,"password":pwd,"checkPass":repwd,"tel":tel,
                "realName":name,"haveRoleList":[role],"state":state}
        return self.session.post('http://192.168.163.131/smart_parking_bg/staff/insert', json=data)