from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host

# 巡检地点
class Actionzhswxjdd():

    def __init__(self):
        self.session = Common.get_session()

    # 添加-【添加】按钮
    def do_tianjia(self):
        head = {'Authorization':ActionLoginApi().get_login()}
        json = {"address": "恩恩额",
                "id": 5,
                "pointName": "",
                "pointNo": "",
                "remark": ""}

        return self.session.post(f'http://{host}/water_bg/point/addPoint',headers=head,json=json)


    # 修改-【修改】按钮
    def do_xiugai_xiugaianniu(self):
        head = {'Authorization':ActionLoginApi().get_login()}
        json = {"address": "湖北武汉",
                "id": 10,
                "pointName": "江春",
                "pointNo": "P0006",
                "remark": "有的"}

        return self.session.post(f'http://{host}/water_bg/point/updatePoint', headers=head,json=json)

    # 删除
    def do_shanchu(self):
        head = {'Authorization':ActionLoginApi().get_login()}
        params = {"id": 11}
        return self.session.get(f'http://{host}/water_bg/point/deletePoint?id=11',headers=head,params=params)

