from procrss.process_rights_management import ProcessRightsManagement


class ActionRightsManagement:

    def __init__(self):
        self.account = ProcessRightsManagement()

    # 新增账户
    def do_add_account(self, account, pwd, repwd, tel, name):
        self.account.click_rights_management()
        self.account.click_account_management()
        self.account.click_add_bwn()
        self.account.input_account(account)
        self.account.input_password(pwd)
        self.account.reinput_password(repwd)
        self.account.input_tel(tel)
        self.account.input_name(name)
        self.account.click_role_box()
        self.account.click_role()
        self.account.click_recover()
        self.account.click_enable()
        self.account.click_save()