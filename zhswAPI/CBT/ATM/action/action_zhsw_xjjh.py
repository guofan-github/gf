from CBT.ATM.action.action_login_api import ActionLoginApi
from CBT.ATM.common.common import Common
from CBT.ATM.common.ip import host

# 巡检计划
class Actionzhswxjjh():

    def __init__(self):
        self.session = Common.get_session()


    # 巡检计划

    # 添加-【添加】
    def do_tianjia(self):

        head = {'Authorization':ActionLoginApi().get_login()}

        json ={"planNo":"5555",
               "planName":"55555",
               "patType":1,
               "patCycle":4,
               "startDate":"2022-06-20T16:00:00.000Z",
               "endDate":"2022-06-28T16:00:00.000Z",
               "remark":"55"}

        return self.session.post(f'http://{host}/water_bg/patrolpoint/add',json=json,headers=head)

    # 查看
    def do_chakan(self):
        head = {'Authorization': ActionLoginApi().get_login()}

        return self.session.get(f'http://{host}/water_bg/patrolpoint/findById?id=1',headers=head)

    # 查看-添加任务
    def do_chakan_tianjia(self):

        head = {'Authorization':ActionLoginApi().get_login()}

        return self.session.get(f'http://{host}/water_bg/patrolpoint/findById?id=1',headers=head)

    # 查看-添加任务-【添加】
    def do_chakan_tianjiaer(self):

        head = {'Authorization':ActionLoginApi().get_login()}

        json = {"taskName":"来来来",
                 "taskType":"plan",
                 "startDate":"2022-06-07T16:00:00.000Z",
                "endDate":"2022-06-13T16:00:00.000Z",
                "executor":"lwl",
                "points":[{"id":10,"pointNo":"P0006","pointName":"江春","address":"湖北武汉","devNum":2000,"remark":"有的","devId":"null"}],"planId":1}
        return self.session.post(f'http://{host}/water_bg/patrolTask/addtask',json=json,headers=head)
