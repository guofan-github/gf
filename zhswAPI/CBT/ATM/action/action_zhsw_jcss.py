from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host


class Actionjcss():

    def __init__(self):
        self.session = Common.get_session()

    def do_bengzhan(self):
        head = {
            'Authorization':ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/base/getBaseType?id=9', headers=head)

    def do_xinzeng(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/base/twoBase',headers=head)

    def do_xinzengqueding(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        data = {"name":"lbw","longitude":"66",
                "latitude":"66","useTime":"2022-06-20T16:00:00.000Z",
                "address":"卢本伟广场",
                "describe":"从现在开始，这里叫做卢本伟广场"}
        return self.session.post(f'http://{host}/water_bg/base/addChildBase', headers=head, json=data)

    def do_bianji(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        data = {"id": 1, "baseId": 8, "name":"lbw","longitude":66,"latitude":6,"useTime":"2021-03-09","address":"卢本伟广场", "describe":"从现在开始这里叫做卢本伟广场"}
        return self.session.post(f'http://{host}/water_bg/base/updateBaseType',headers=head,json=data)

    def do_shenqingliebiao(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        data ={
            "baseId": 8
        }
        return self.session.get(f'http://{host}/water_bg/ask/getBaseMyself?baseId=8',headers=head, data=data)

    def do_xiangqing(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }

        return self.session.get(f'http://{host}/water_bg/child/getChild?id=4', headers=head)

    def do_xiugai(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        data = {"id":17,"stockChildId":4,"childName":"Name","childStatus":"良好"}
        return self.session.post(f'http://{host}/water_bg/child/updateChild',headers=head, json=data)

    def do_tianjia(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        data = {"stockChildId":4,"childName":"帅","childStatus":"良好"}
        return self.session.post(f'http://{host}/water_bg/child/addChild', headers=head, json=data)

    def do_shenqing2(self):
        head = {
            'Authorization': ActionLoginApi().get_login()
        }
        data = {
            "id": 4,
            "reason": "来几台机器，搞快点",
            "askNum": 66
        }
        return self.session.get(f'http://{host}/water_bg/ask/askStock?id=4&reason='
                                f'%E6%9D%A5%E5%87%A0%E5%8F%B0%E6%9C%BA%E5%99%A8%E'
                                f'F%BC%8C%E6%90%9E%E5%BF%AB%E7%82%B9&askNum=66',
                                headers=head, data=data)
