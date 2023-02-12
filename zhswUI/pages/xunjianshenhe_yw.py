
import time


# 页面元素定位层
from pages.businesspage import businesspage
from util.config import host_port


class EmployeePage(businesspage):

    def __init__(self):
        businesspage.__init__(self)
        # 进入巡检审核页面
        self.driver.get(f"http://{host_port}/water/#/patrol/check")

        time.sleep(2)

    #定位审核按钮
    def get_xjshh_shh(self):
        return self.driver.find_element_by_xpath('//tbody/tr[1]/td[7]//button[2]')

    #定位审核通过选项
    def get_xjshh_shtg(self):
        return self.driver.find_element_by_xpath('//div[2]/form/div[1]/div/div/div/label[1]/span[1]/span')

    #定位审核建议输入框
    def get_xjshh_shhjy(self):
        return self.driver.find_element_by_xpath('//div[2]/form/div[2]/div/div/div/div/textarea')

    #定位提交按钮
    def get_xjshh_tj(self):
        return self.driver.find_element_by_xpath('//main/div[3]/div[5]/div/div[3]/div/button[2]')

    #定位查看详情按钮
    def get_xjshh_ckxq(self):
        return self.driver.find_element_by_xpath('//table/tbody/tr[1]/td[7]/div/button[1]/span')

    #定位取消按钮
    def get_xjshh_qx(self):
        return self.driver.find_element_by_xpath('//div[5]/div/div[3]/div/button[1]')

    #定位审核不通过按钮
    def get_xjshh_btg(self):
        return self.driver.find_element_by_xpath('//div[5]/div/div[3]/div/button[1]')

    #定位弹出信息
    def get_xjshh_tc(self):
        return self.driver.find_element_by_xpath('/html/body/div[2]/p')
    #定位查看详情弹出信息
    def get_xjshh_tcts(self):
        return self.driver.find_element_by_xpath('//main/div[3]/div[4]/div/div[1]/span')

#操作层
class  EmployeeHandle(EmployeePage):

    def __init__(self):
        EmployeePage.__init__(self)

    #点击审核按钮
    def click_xjshh_shh(self):
        self.get_xjshh_shh().click()
        time.sleep(1)

    #点击审核通过
    def click_xjshh_shtg(self):
        self.get_xjshh_shtg().click()
        time.sleep(1)

    #输入审核建议
    def send_xjshh_shhjy(self, x):
        self.get_xjshh_shhjy().send_keys(x)

    #点击提交
    def click_xjshh_tj(self):
        self.get_xjshh_tj().click()

    #点击取消
    def click_xjshh_qx(self):
        self.get_xjshh_qx().click()

    #点击查看详情
    def click_xjshh_ckxq(self):
        self.get_xjshh_ckxq().click()

    #获取弹出文本信息
    def get_wbxx(self):
        time.sleep(1)
        return self.get_xjshh_tc().text

    #获取弹出提示文本信息
    def get_tcwbxx(self):
        time.sleep(1)
        return self.get_xjshh_tcts().text

#业务层
class EmployeeBusiness(EmployeeHandle):

    def __init__(self):
        EmployeeHandle.__init__(self)

    #审核巡检任务业务
    def xjshh_shenhexunjianrenwu(self, shhyj):
        self.click_xjshh_shh()
        self.click_xjshh_shtg()
        self.send_xjshh_shhjy(shhyj)
        self.click_xjshh_tj()
    #获取弹窗文本信息
        msg = self.get_wbxx()
        return msg

    #查看详情业务
    def xjshh_chakanxiangqing(self):
        self.click_xjshh_ckxq()
        self.get_tcwbxx()