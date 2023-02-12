from pages.businesspage import businesspage
from util.config import host_port
import time


class ShlbPage(businesspage):

    def __init__(self):
        businesspage.__init__(self)
        self.driver.get(f"http://{host_port}/water/#/buy/list")

    def get_yesclick(self):
        return self.driver.find_element_by_xpath('//*[@id="app"]/section/section'
                                                      '/main/div[3]/div[1]/div/div[4]/'
                                                      'div[2]/table/tbody/tr/td[9]/div/button[1]/i')

    def get_shlbwelcome(self):
        return self.driver.find_element_by_css_selector('body > div.el-message.el-message--success > p')

class ShlbCaozuo(ShlbPage):

    def __init__(self):
        ShlbPage.__init__(self)

    def click_yes(self):
        self.get_yesclick().click()
        time.sleep(1)

    def shlb_text(self):
        return self.get_shlbwelcome().text


class ShlbYewu(ShlbCaozuo):

    def __init__(self):
        ShlbCaozuo.__init__(self)

    def shlb_yewu(self):

        self.click_yes()

        msg = self.shlb_text()

        return msg