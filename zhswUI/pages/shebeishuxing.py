import time


#页面元素定位层
from pages.businesspage import businesspage
from util.config import host_port


class sbsxpage(businesspage):
    def __init__(self):
        businesspage.__init__(self)
        # 进入巡检审核页面
        self.driver.get(f"http://{host_port}/water/#/device/property")

        time.sleep(2)

    #定位压力表选项
    def get_sbsx_ylb(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/section/section/aside/div/div[2]/div/div[1]/div/div/div/div[3]')

    #定位修改按钮
    def get_sbsx_xg(self):
        return self.driver.find_element_by_xpath('//div/div[1]/div/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/button/span')

    #定位属性名称输入框
    def get_sbsx_xgsxmc(self):
        return self.driver.find_element_by_xpath('//div/div[3]/div/div[2]/form/div/div[1]/div/div/div/input')

    #定位计量单位输入框
    def get_sbsx_xgjldw(self):
        return self.driver.find_element_by_xpath('//div/div[3]/div/div[2]/form/div/div[2]/div/div/div/input')

    #定位修改按钮
    def get_sbsx_tcxg(self):
        return self.driver.find_element_by_xpath('//div/div[3]/div/div[3]/div/button[2]/span')

    #定位修改成功信息
    def get_sbsx_xgcg(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

    #定位删除按钮
    def get_sbsx_sc(self):
        return self.driver.find_element_by_xpath('//tr[2]/td[3]/div/span/span/button/span')

    #定位确定删除按钮
    def get_sbsx_qdsc(self):
        return self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/button[2]/span')

    #定位提示信息
    def get_sbsx_xgtsxx(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

    #定位删除成功提示信息
    def get_sbsx_sccg(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

    #定位添加按钮
    def get_sbsx_tj(self):
        return self.driver.find_element_by_xpath('//div/div[1]/div/div[3]/div/button/span')

    #定位属性名称输入框
    def get_sbsx_sxmc(self):
        return self.driver.find_element_by_xpath('//div/div[3]/div/div[2]/form/div/div[1]/div/div/div/input')

    #定位计量单位输入框
    def get_sbsx_jldw(self):
        return self.driver.find_element_by_xpath('//div/div[3]/div/div[2]/form/div/div[2]/div/div/div/input')

    #定位弹窗添加按钮
    def get_sbsx_tctj(self):
        return self.driver.find_element_by_xpath('//div/div[3]/div/div[3]/div/button[2]/span')

    #定位添加成功弹窗
    def get_sbsx_cgtc(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')


#操作层
class sbsxcaozuo(sbsxpage):
    def __init__(self):
        sbsxpage.__init__(self)

    #点击压力表
    def click_sbsx_ylb(self):
        self.get_sbsx_ylb().click()

    #点击添加按钮
    def click_sbsx_tj(self):
        self.get_sbsx_tj().click()

    #添加界面输入属性名称
    def send_sbsx_sxmc(self,sxm):
        self.get_sbsx_sxmc().send_keys(sxm)

    #添加界面输入计量单位
    def send_sbsx_jldw(self,dwm):
        self.get_sbsx_jldw().send_keys(dwm)

    #点击添加
    def click_sbsx_tctj(self):
        self.get_sbsx_tctj().click()


    #获取添加成功文本
    def get_sbsx_cgts(self):
        time.sleep(1)
        return self.get_sbsx_cgtc().text

    #点击修改按钮
    def click_sbsx_xg(self):
        self.get_sbsx_xg().click()

    #清空属性名称
    def clear_sbsx_xgsxmc(self):
        self.get_sbsx_xgsxmc().clear()

    #输入修改属性名称
    def send_sbsx_xgsxmc(self,sxm):
        self.get_sbsx_xgsxmc().send_keys(sxm)

    #清空计量单位
    def clear_sbsx_xgjldw(self):
        self.get_sbsx_xgjldw().clear()

    #修改计量单位
    def send_sbsx_xgjldw(self,dwm):
        self.get_sbsx_xgjldw().send_keys(dwm)

    #点击弹窗中的修改按纽
    def click_sbsx_tcxg(self):
        self.get_sbsx_tcxg().click()

    #获取修改的弹窗信息
    def get_sbsx_hqxx(self):
        time.sleep(1)
        return self.get_sbsx_xgcg().text

    #点击删除按钮
    def click_sbsx_sc(self):
        self.get_sbsx_sc().click()


    #点击确定
    def click_sbsx_qd(self):
        self.get_sbsx_qdsc().click()


    #获取删除成功提示信息
    def get_sbsx_sccghq(self):
        time.sleep(1)
        return self.get_sbsx_sccg().text

#业务层
class sbsxyewu(sbsxcaozuo):
    def __init__(self):
        sbsxcaozuo.__init__(self)

    #修改业务
    def sbsx_xiugaiyewu(self,xgsxmc,xgjldw):
        self.click_sbsx_ylb()
        self.click_sbsx_xg()
        self.clear_sbsx_xgsxmc()
        self.clear_sbsx_xgjldw()
        self.send_sbsx_xgsxmc(xgsxmc)
        self.send_sbsx_xgjldw(xgjldw)
        self.click_sbsx_tcxg()
        sg = self.get_sbsx_hqxx()
        return sg

    #添加业务
    def sbsx_tianjiayewu(self,sxmc,jldw):
        self.click_sbsx_ylb()
        self.click_sbsx_tj()
        self.send_sbsx_sxmc(sxmc)
        self.send_sbsx_jldw(jldw)
        self.click_sbsx_tctj()
        msg = self.get_sbsx_cgts()

        print(msg)
        return msg

    #删除业务
    def sbxz_shanchuyewu(self):
        self.click_sbsx_ylb()
        self.click_sbsx_sc()
        self.click_sbsx_qd()
        sc = self.get_sbsx_sccghq()
        print(sc)
        return sc

if __name__ == '__main__':
    sbsxyewu().sbsx_tianjiayewu(1,2)