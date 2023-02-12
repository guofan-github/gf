import time
from WebDriver.get_fact import GetFact
from util.config import host_port
from pages.businesspage import businesspage


# 元素定位
class ypgdpage(businesspage):
    def __init__(self):
        businesspage.__init__(self)
        self.driver.get(f'http://{host_port}/water/#/worker/yet')
        time.sleep(2)

    def get_ypgd_qsh(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[15]/div/button[1]/span')

# 操作层
class ypgdcaozuo(ypgdpage):
    def __init__(self):
        ypgdpage.__init__(self)

    def click_ypgd_qsh(self):
        self.get_ypgd_qsh().click()
        time.sleep(2)

# 业务层
class ypgdyewu(ypgdcaozuo):
    def __init__(self):
        ypgdcaozuo.__init__(self)

    def add_ypgd_notice(self):
        self.click_ypgd_qsh()

