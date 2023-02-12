from selenium.webdriver.remote.command import Command

from pages.businesspage import businesspage
from util.config import host_port
import time

class yshgdpage(businesspage):

    def __init__(self):
        businesspage.__init__(self)
        self.driver.get(f"http://{host_port}/water/#/worker/ischeck")

    def get_yshgd_shan_chu(self):
        return self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/section/main/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[16]/div/button/span')

    def get_yshgd_que_ding(self):
        return self.driver.find_element_by_css_selector(
            'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span')

class yshgdcaozuo(yshgdpage):

    def __init__(self):
        yshgdpage.__init__(self)

    def click_shanchu(self):
        self.get_yshgd_shan_chu().click()

    def click_yshgd_queding(self):
        self.get_yshgd_que_ding().click()
        time.sleep(3)
        # return self.driver.switch_to.alert.text
        # alert_obj = self.driver.switch_to.alert
        # alert_obj.accept()
        # return self.driver.switch_to.alert.text

        # print(alert_obj.text)
        # return alert_obj
        # alert_obj.accept()


    # def text_yshgd(self):
    #     alert_obj = self.driver.switch_to.alert
    #     alert_obj.accept()
    #     print(alert_obj.text)
    #     return alert_obj.text





class yshgdyewu(yshgdcaozuo):

    def __init__(self):
        yshgdcaozuo.__init__(self)

    def yshgd_yewu(self):

        self.click_shanchu()

        self.click_yshgd_queding()
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text







if __name__ == '__main__':
    yshgdyewu().yshgd_yewu()