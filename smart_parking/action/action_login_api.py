from common.common import Common


class ActionLoginApi:

    def __init__(self):
        self.session = Common.get_session()

    # 验证码
    def do_code(self):
        return self.session.get('http://192.168.163.131/smart_parking_bg/login/captcha')

    # 登录
    def do_login_api(self, user, pwd, code):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
                    'Accept': 'application/json, text/plain, */*'}
        body = {"accountName": user, "password": pwd,
                "captcha": code, "captchaKey": "0000"}
        return self.session.post('http://192.168.163.131/smart_parking_bg/login', headers=header, json=body)

