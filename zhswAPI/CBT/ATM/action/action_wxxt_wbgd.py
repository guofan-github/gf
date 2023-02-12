from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host


class ActiontjgdApi:

    def __init__(self):
        self.session = Common.get_session()

    def do_jrmk(self):
        body ={"dealWithDate":"","endDate":""}
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/repiar/circular',json=body,headers=hader)

    def do_tjgd(self):
        body = {"reflectPeople":"PYY",
                "source":"gfhbb",
                "phone":"13133450853",
                "email":"1727254353@qq.com",
                "reflectUnit":"计划生育小组",
                "reflectArea":"弗雷尔卓德",
                "reflectContent":"猪妹生了",
                "reflectClass":"高",
                "happenDate":"2022-06-22 00:00:00",
                "happenArea":"嚎哭深渊",
                "eventId":3,
                "endDate":"2022-07-28 00:00:00"}
        hader = {
            'Authorization':ActionLoginApi().get_login()
        }
        return self.session.post(f'http://{host}/water_bg/repair/add', json=body, headers=hader)

    def do_cz(self):
        body = {"state":1,
                "source":"",
                "eventId":"",
                "reflectPeople":"",
                "phone":"",
                "reflectUnit":"",
                "reflectArea":"",
                "pappenArea":"",
                "pageIndex":1,
                "happenDate":"",
                "endDate":"",
                "happenArea":"ada"}
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.post(f'http://{host}/water_bg/worker/list',json= body,headers=hader)

    def do_wpgdcx(self):
        body = {"state":1,
                "source":"电子邮件",
                "eventId":"",
                "reflectPeople":"",
                "phone":"",
                "reflectUnit":"",
                "reflectArea":"江夏区",
                "pappenArea":"",
                "pageIndex":1,
                "happenDate":"",
                "endDate":""}
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.post(f'http://{host}/water_bg/worker/list',json= body, headers=hader)

    def do_wpgdxg(self):
        body = {"id":3,
                "reflectPeople":"王五",
                "source":"电子邮件",
                "phone":"15971846413",
                "email":"132148@qq.com",
                "reflectUnit":"市一中",
                "reflectArea":"江夏区",
                "reflectClass":"水流小",
                "happenDate":"2021-03-11 14:28:47",
                "happenArea":"武汉市一中",
                "eventId":1,
                "endDate":"2021-03-13 14:29:11",
                "state":1,
                "stateName":"未指派"}
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.post(f'http://{host}/water_bg/repair/update',json=body,headers=hader)

    def do_wpgdsc(self):
        body = {id : 22}
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/repair/delete?id=22',headers=hader)

    def do_wpgdfy(self):
        body = {"state":1,
                "source":"",
                "eventId":"",
                "reflectPeople":"",
                "phone":"",
                "reflectUnit":"",
                "reflectArea":"",
                "pappenArea":"",
                "pageIndex":4,
                "happenDate":"",
                "endDate":""}
        hader = {
            'Authorization': ActionLoginApi().get_login()
        }
        return self.session.get(f'http://{host}/water_bg/worker/list', json= body, headers=hader)