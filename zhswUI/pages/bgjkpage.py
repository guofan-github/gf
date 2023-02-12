import time
from WebDriver.get_fact import GetFact
from pages.businesspage import businesspage
from util.config import host_port

# 元素定位
class bgjkpage(businesspage):
    def __init__(self):
        businesspage.__init__(self)
        self.driver.get(f'http://{host_port}/water/#/monitor/boom')
        time.sleep(2)


    # 爆管监控
    def get_bgjk(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/div[2]/div[1]/div[1]/div[1]')

    #                                         / html / body / div / section / section / main / div[3] / div[2] / div[1] / div[1] / div[1]
    # 【开始监控】按钮
    def get_bgjk_ksjk(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/div[1]/div/div[2]/button/span')
    # 【3D地球】
    def get_bgjk_diqiu(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/div[2]/div[1]/div[6]/div[3]/div')
    # 【显示网路】按钮
    def get_bgjk_xswl(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/div[2]/div[1]/div[6]/div[1]/span[2]')
    # 【停止监控】按钮
    def get_bgjk_tzjk(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/div[1]/div/div[2]/button/span')

# 操作层
class bgjkcaozuo(bgjkpage):
    def __init__(self):
        bgjkpage.__init__(self)

    # 爆管监控
    def click_bgjk(self):
        self.get_bgjk().click()
        time.sleep(2)

    # 【开始监控】按钮
    def click_bgjk_ksjk(self):
        self.get_bgjk_ksjk().click()
        time.sleep(2)

    # 【地球】按钮
    def click_bgjk_diqiu(self):
        self.get_bgjk_diqiu().click()
        time.sleep(2)

     # 【显示网路】按钮
    def click_bgjk_xswl(self):
        self.get_bgjk_xswl().click()
        time.sleep(2)

    # 【停止监控】按钮
    def click_bgjk_tzjk(self):
        self.get_bgjk_tzjk().click()
        time.sleep(2)

# 业务层
class bgjkyewu(bgjkcaozuo):
    def __init__(self):
        bgjkcaozuo.__init__(self)

    def add_bgjk_notice(self):
        self.click_bgjk()
        self.click_bgjk_ksjk()
        self.click_bgjk_diqiu()
        self.click_bgjk_xswl()
        self.click_bgjk_tzjk()

