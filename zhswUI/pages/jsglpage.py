import time
from WebDriver.get_fact import GetFact
from util.config import host_port
from pages.businesspage import businesspage


# 元素定位层
class jsglpage(businesspage):
    def __init__(self):
        businesspage.__init__(self)
        self.driver.get(f'http://{host_port}/water/#/role/manager')
        time.sleep(2)

# 分配权限
    def get_jsgl_fpqx(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[1]/div[3]/table/tbody/tr[3]/td[3]/div/button/span')
    # 系统管理
    def get_jsgl_xtgl(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/span[2]')
    # 角色管理
    def get_jsgl_jsgl(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/label/span/span')
    # 【确定】按钮
    def get_jsgl_qd(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[2]/div/div[3]/div/button[2]/span')
    # 断言 【授权成功】
    def get_jsgl_sqcg(self):
        return self.driver.find_element_by_xpath('//div[@class="el-message el-message--success"]//p')


# 操作层
class jsglcaozuo(jsglpage):
    def __init__(self):
        jsglpage.__init__(self)

    # 分配权限
    def click_jsgl_jspeqx(self):
        self.get_jsgl_fpqx().click()

    # 分配权限-系统管理
    def click_jsgl_jsxtgl(self):
        self.get_jsgl_xtgl().click()

    # 系统管理-角色管理
    def click_jsgl_jsjsgl(self):
        self.get_jsgl_jsgl().click()

    # 【确定】按钮
    def click_jsgl_qdan(self):
        self.get_jsgl_qd().click()


    # 断言【授权成功】文本
    def get_jsgl_jssqcg(self):
        return self.get_jsgl_sqcg().text


# 业务层

class jsglyewu(jsglcaozuo):
    def __init__(self):
        jsglcaozuo.__init__(self)

    def add_xjjh_notice(self):
        # 分配权限
        self.click_jsgl_jspeqx()
        # 分配权限-系统管理
        self.click_jsgl_jsxtgl()
        # 系统管理-角色管理
        self.click_jsgl_jsjsgl()
        # 【确定】按钮
        self.click_jsgl_qdan()
        # 断言【授权成功】文本
        ddd = self.get_jsgl_jssqcg()
        return ddd
