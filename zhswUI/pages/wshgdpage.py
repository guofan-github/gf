import time



# 页面元素定位层
from pages.businesspage import businesspage
from util.config import host_port


class wshgdpage(businesspage):

    def __init__(self):
        businesspage.__init__(self)
        # 进入页面
        self.driver.get(f'http://{host_port}/water/#/worker/check')
        time.sleep(3)

    # 审核
    def get_wshgd_shenhe(self):
        return self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[17]/div/button[1]/span')
    # 审核成功定位
    def get_wshgd_tcdingwei(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

# 操作层
class wshgdcaozuo(wshgdpage):

    def __init__(self):
        wshgdpage.__init__(self)

    # 点击审核按钮
    def click_wshgd_shenhe(self):
        self.get_wshgd_shenhe().click()
        time.sleep(1)

    # 获取弹窗文本
    def get_wshgd_gctext(self):
        return self.get_wshgd_tcdingwei().text

# 业务层
class wshgdyewu(wshgdcaozuo):

    def __init__(self):
        wshgdcaozuo.__init__(self)

    # 审核
    def shenhe_wshgd(self):
        # 点击审核
        self.click_wshgd_shenhe()
        msg = self.get_wshgd_gctext()
        return msg





