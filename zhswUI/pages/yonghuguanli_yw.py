import time


#页面元素定位层
from pages.businesspage import businesspage
from util.config import host_port


class yhglpage(businesspage):
    def __init__(self):
        businesspage.__init__(self)
        # 进入巡检审核页面
        self.driver.get(f"http://{host_port}/water/#/user/manager")

        time.sleep(2)

    #定位添加按钮


    def get_yhgl_tj(self):
        return self.driver.find_element_by_xpath('//div[3]/form/div[4]/div/button')

    #定位姓名输入框
    def get_yhgl_xm(self):
        return self.driver.find_element_by_xpath('//div[3]/div/div[2]/form/div[1]/div/div[1]/input')

    #定位用户名输入框
    def get_yhgl_yhm(self):
        return self.driver.find_element_by_xpath('//div[3]/div[3]/div/div[2]/form/div[2]/div/div/input')

    #定位密码输入框
    def get_yhgl_mm(self):
        return self.driver.find_element_by_xpath('//div[3]/div/div[2]/form/div[3]/div/div/input')

    #定位电话输入框
    def get_yhgl_dh(self):
        return self.driver.find_element_by_xpath('//div[3]/div/div[2]/form/div[3]/div/div/input')

    #定位职位下拉选择框
    def get_yhgl_zhw(self):
        return self.driver.find_element_by_xpath('//div[3]/div/div[2]/form/div[5]/div/div/div/input')

    #定位水务经理选项
    def get_yhgl_swjl(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')

    #定位确定按钮
    def get_yhgl_qd(self):
        return self.driver.find_element_by_xpath('//div[3]/div[3]/div/div[3]/div/button[2]/span')

    #定位页码按钮
    def get_yhgl_fy(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

    #定位修改按钮
    def get_yhgl_xg(self):
        return self.driver.find_element_by_xpath('//div[5]/div[2]/table/tbody/tr[1]/td[10]/div/button[1]/span')

    #定位修改页面姓名输入框
    def get_yhgl_xgxm(self):
        return self.driver.find_element_by_xpath('//div[3]/div[4]/div/div[2]/form/div[1]/div/div/input')

    #定位修改页面用户名输入框
    def get_yhgl_xgyhm(self):
        return self.driver.find_element_by_xpath('//div[3]/div[4]/div/div[2]/form/div[2]/div/div/input')

    #定位修改页面密码输入框
    def get_yhgl_xgmm(self):
        return self.driver.find_element_by_xpath('//div[4]/div/div[2]/form/div[3]/div/div/input')

    #定位修改页面电话输入框
    def get_yhgl_xgdh(self):
        return self.driver.find_element_by_xpath('//div[4]/div/div[2]/form/div[4]/div/div/input')

    #定位修改页面职位下拉选择框
    def get_yhgl_xgzw(self):
        return self.driver.find_element_by_xpath('//div[3]/div[4]/div/div[2]/form/div[5]/div/div/div/input')

    #定位修改页面植职务选项
    def get_yhgl_xgswzj(self):
        return self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')

    #定位确定按钮
    def get_yhgl_xgqd(self):
        return self.driver.find_element_by_xpath('//div[3]/div[4]/div/div[3]/div/button[2]/span')

    #定位弹出信息
    def get_yhgl_tcxx(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

    #定位修改弹出信息
    def get_yhgl_xgtcxx(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

#操作层
class yhglcaozuo(yhglpage):
    def __init__(self):
        yhglpage.__init__(self)

    #点击添加按钮
    def click_yhgl_tj(self):
        self.get_yhgl_tj().click()

    #输入姓名
    def send_yhgl_xm(self,xm):
        self.get_yhgl_xm().send_keys(xm)

    #输入用户名
    def send_yhgl_yhm(self,yhm):
        self.get_yhgl_yhm().send_keys(yhm)

    #输入密码
    def send_yhgl_mm(self,mm):
        self.get_yhgl_mm().send_keys(mm)

    #输入电话
    def send_yhgl_dh(self,dh):
        self.get_yhgl_dh().send_keys(dh)

    #选择职务
    def click_yhgl_zw(self):
        self.get_yhgl_zhw().click()

    #选择水务经理
    def click_yhgl_swjl(self):
        self.get_yhgl_swjl().click()

    #点击确定
    def click_yhgl_qd(self):
        self.get_yhgl_qd().click()

    #点击翻页按钮
    def click_yhgl_fy(self):
        self.get_yhgl_fy().click()

    #点击修改
    def click_yhgl_xg(self):
        self.get_yhgl_xg().click()

    #清空姓名框
    def clear_yhgl_qkxm(self):
        self.get_yhgl_xgxm().clear()

    #修改姓名
    def send_yhgl_xgxm(self,xgxm):
        self.get_yhgl_xgxm().send_keys(xgxm)

    #清空电话
    def clear_yhgl_qkdh(self):
        self.get_yhgl_xgdh().clear()

    #修改电话
    def send_yhgl_xgdh(self,xgdh):
        self.get_yhgl_xgdh().send_keys(xgdh)

    #点击确定
    def click_yhgl_xgqd(self):
        self.get_yhgl_xgqd().click()

    #获取文本信息
    def get_yhgl_hqxx(self):
        time.sleep(1)
        return self.get_yhgl_tcxx().text

    #获取弹出修改成功信息
    def get_yhgl_hqxgxx(self):
        time.sleep(1)
        return self.get_yhgl_xgtcxx().text

#业务层
class yhglyewu(yhglcaozuo):
    def __init__(self):
        yhglcaozuo.__init__(self)

    #用户管理添加业务
    def yhgl_tianjiayonghu(self,q,w,e,r):
        self.click_yhgl_tj()
        self.send_yhgl_xm(q)
        self.send_yhgl_yhm(w)
        self.send_yhgl_mm(e)
        self.send_yhgl_dh(r)
        self.click_yhgl_zw()
        self.click_yhgl_swjl()
        self.click_yhgl_qd()
        wb = self.get_yhgl_hqxx()
        return wb

    #用户管理修改用户信息业务
    def yhgl_xiugaiyonghuxinxi(self,y,u):
        self.click_yhgl_xg()
        self.clear_yhgl_qkxm()
        self.clear_yhgl_qkdh()
        self.send_yhgl_xgxm(y)
        self.send_yhgl_xgdh(u)
        self.click_yhgl_xgqd()
        xgfk = self.get_yhgl_hqxgxx()
        return xgfk

