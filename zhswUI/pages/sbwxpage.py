import time

from pages.businesspage import businesspage
from util.config import host_port


class sbwxpage(businesspage):

    def __init__(self):
        businesspage.__init__(self)
        # 进入页面
        self.driver.get(f'http://{host_port}/water/#/base/repair')

    # 状态选择框
    def get_sbwx_zhuangtaixzk(self):
        return self.driver.find_element_by_css_selector('input[placeholder="请选择"]')

    # 选择状态
    def get_sbwx_zhuangtai(self):
        return self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')

    # 查询
    def get_sbwx_chaxun(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/form/div[3]/div/button[1]/span')

    # 完成检修
    def get_sbwx_wanchengjx(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/button[1]')

    # 完成弹窗
    def get_sbwx_wctanchuang(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

# 操作层
class sbwxcaozuo(sbwxpage):

    def __init__(self):
        sbwxpage.__init__(self)

    # 点击状态选择框
    def click_sbwx_zhuangtaixzk(self):
        self.get_sbwx_zhuangtaixzk().click()
        time.sleep(1)

    # 点击选择状态
    def click_sbwx_zhuangtai(self):
        self.get_sbwx_zhuangtai().click()

    # 点击查询
    def click_sbwx_chaxun(self):
        self.get_sbwx_chaxun().click()

    # 点击完成检修
    def click_sbwx_wcjianxiu(self):
        self.get_sbwx_wanchengjx().click()
        time.sleep(1)

    # 获取弹窗文本
    def get_tctext(self):
        return self.get_sbwx_wctanchuang().text

# 业务层
class sbwxyewu(sbwxcaozuo):

    def __init__(self):
        sbwxcaozuo.__init__(self)

    # 设备维修
    def wcjx_sbwx(self):
        # 点击状态选择框
        self.click_sbwx_zhuangtaixzk()
        # 点击状态
        self.click_sbwx_zhuangtai()
        # 点击查询
        self.click_sbwx_chaxun()
        # 点击完成检修
        self.click_sbwx_wcjianxiu()
        # 获取弹窗文本
        msg = self.get_tctext()
        return msg
