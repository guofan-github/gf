import time
from WebDriver.get_fact import GetFact
from util.config import host_port
from pages.businesspage import businesspage


# 元素定位
class wpgdpage(businesspage):
    def __init__(self):
        businesspage.__init__(self)
        self.driver.get(f'http://{host_port}/water/#/worker/not')
        time.sleep(2)

    # 添加工单
    def get_wpgd_tjgd(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/form/div[11]/div/button/span')

    # 添加工单-反映人
    def get_wpgd_fyr(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[1]/div[1]/div/div/div[1]/input')

    def get_wpgd_fyrh(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[1]/div[2]/div/div/div/input')

    # 添加工单-电话
    def get_wpgd_number(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[2]/div[1]/div/div/div[1]/input')

    # 添加工单-邮箱
    def get_wpgd_email(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div[1]/input')

    # 添加工单-反应单位
    # def get_wpgd_fygd(self):
    #     return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[3]/div[1]/div/div/div/input')
    # def get_wpgd_fygdh(self):
    #     return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[3]/div[2]/div/div/div[1]/input')
    # 添加工单-反应内容
    def get_wpgd_fynr(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[4]/div[1]/div/div/div[1]/input')

    def get_wpgd_fynrh(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[4]/div[2]/div/div/div/div[1]/input')

    def get_wpgd_fynrhtc(self):
        return self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]')

    # 添加工单-发生地点
    def get_wpgd_fsdd(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[5]/div[2]/div/div/div[1]/input')

    # 添加工单-事件等级
    def get_wpgd_sjdj(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[6]/div[1]/div/div/div/div/input')

    def get_wpgd_sjdjtc(self):
        return self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]')

    # 添加工单-截止日期
    def get_wpgd_jzrq(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[6]/div[2]/div/div/div/input')

    def get_wpgd_jzrqxlk(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[1]/div/div[3]/table[1]/tbody/tr[6]/td[4]/div/span')


    def get_wpgd_jzrqqd(self):
        return self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[2]/span')

    # 添加工单-【确定】按钮
    def get_wpgd_qd(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[3]/div/button[2]/span')

    # 断言 【添加成功】
    def get_wpgd_tjcg(self):
        return self.driver.find_element_by_xpath('//div[@class="el-message el-message--success"]//p')


# 操作层
class wpgdcaozuo(wpgdpage):
    def __init__(self):
        wpgdpage.__init__(self)

    # 添加工单
    def click_wpgd_tjgd(self):
        self.get_wpgd_tjgd().click()
        time.sleep(2)

    # 添加工单-反应人
    def send_wpgd_fyr(self):
        self.get_wpgd_fyr().send_keys('888')

    def send_wpgd_fyrh(self):
        self.get_wpgd_fyrh().send_keys('999')

    # 添加工单-电话
    def send_wpgd_number(self):
        self.get_wpgd_number().send_keys('18391447305')

    # 添加工单-邮箱
    def send_wpgd_email(self):
        self.get_wpgd_email().send_keys('770252619@qq.com')

    # # 添加工单-反映单位
    # def get_wpgd_fygd(self):
    #     self.get_wpgd_fygd().send_keys('今天15号')
    # def send_wpgd_fygdh(self):
    #     self.get_wpgd_fygdh().send_keys('今天温度快40了')

    # 添加工单-反映内容
    def send_wpgd_fynr(self):
        self.get_wpgd_fynr().send_keys('郭凡今天也是打地鼠的一天')

    def send_wpgd_fynrh(self):
        self.get_wpgd_fynrh().click()
        time.sleep(2)

    def send_wpgd_fynrhtc(self):
        self.get_wpgd_fynrhtc().click()
        time.sleep(2)

    # 添加工单-反映地点
    def send_wpgd_fsdd(self):
        self.get_wpgd_fsdd().send_keys('也可以说是救火')

    # 添加工单-事件等级
    def click_wpgd_sjdj(self):
        self.get_wpgd_sjdj().click()
        time.sleep(2)

    def click_wpgd_sjdjtc(self):
        self.get_wpgd_sjdjtc().click()
        time.sleep(2)

    # 添加工单-截止日期
    def click_wpgd_jzrq(self):
        self.get_wpgd_jzrq().click()
        time.sleep(2)

    def click_wpgd_jzrqxlk(self):
        self.get_wpgd_jzrqxlk().click()
        time.sleep(2)

    def click_wpgd_jzrqqd(self):
        self.get_wpgd_jzrqqd().click()
        time.sleep(2)

    # 【确定】按钮
    def click_wpgd_qd(self):
        self.get_wpgd_qd().click()
        time.sleep(2)

    # 断言 【添加成功】文本
    def get_wpgd_tjcgdy(self):
        return self.get_wpgd_tjcg().text


# 业务层
class wpgdyewu(wpgdcaozuo):
    def __init__(self):
        wpgdcaozuo.__init__(self)

    def add_wpgd_notice(self):
        self.click_wpgd_tjgd()
        self.send_wpgd_fyr()
        self.send_wpgd_fyrh()
        self.send_wpgd_number()
        self.send_wpgd_email()
        # self.get_wpgd_fygd()
        # self.send_wpgd_fygdh()
        self.send_wpgd_fynr()
        self.send_wpgd_fynrh()
        self.send_wpgd_fsdd()
        self.click_wpgd_sjdj()
        self.click_wpgd_sjdjtc()
        self.click_wpgd_jzrq()
        self.click_wpgd_jzrqxlk()
        self.click_wpgd_jzrqqd()
        self.click_wpgd_qd()
        ttt = self.get_wpgd_tjcgdy()
        return ttt
