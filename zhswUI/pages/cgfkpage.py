import time
from pages.businesspage import businesspage

# 元素定位
from util.config import host_port


class cgfkpage(businesspage):
    def __init__(self):
        businesspage.__init__(self)
        self.driver.get(f'http://{host_port}/water/#/buy/buyback')
        time.sleep(2)

    # 翻页第3页
    def get_cgfk_fanye(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/div[2]/ul/li[3]')

    # 【提交】按钮
    def get_cgfk_tj(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[3]/td[14]/div/button/span')

    # 反馈采购清单-实际单价
    def get_cgfk_sjdj(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[1]/div/div/input')
    # 反馈采购清单-实际数量
    def get_cgfk_sjsl(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[2]/div/div/input')
    # 反馈采购清单-实际金额
    def get_cgfk_sjje(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[3]/div/div/input')
     # 【确定】按钮
    def get_cgfk_qd(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[3]/div/button[2]/span')


# 操作层
class cgfkcaozuo(cgfkpage):
    def __init__(self):
        cgfkpage.__init__(self)

    # 提交到第3页
    def click_cgfk_fanye(self):
        self.get_cgfk_fanye().click()

    # 【提交】按钮
    def click_cgfk_tj(self):
        self.get_cgfk_tj().click()

    # 反馈采购清单-实际单价
    def send_cgfk_sjdj(self):
        self.get_cgfk_sjdj().send_keys('123')
    # 反馈采购清单-实际数量
    def send_cgfk_sjsl(self):
        self.get_cgfk_sjsl().send_keys('852')
    # 反馈采购清单-实际金额
    def send_cgfk_sjje(self):
        self.get_cgfk_sjje().send_keys('159')

    # 【确定】按钮
    def send_cgfk_qd(self):
        self.get_cgfk_qd().click()

# 业务层
class cgfkyewu(cgfkcaozuo):
    def __init__(self):
        cgfkcaozuo.__init__(self)
    def add_cgfk_notice(self):
        self.click_cgfk_fanye()
        self.click_cgfk_tj()
        self.send_cgfk_sjdj()
        self.send_cgfk_sjsl()
        self.send_cgfk_sjje()
        self.send_cgfk_qd()

