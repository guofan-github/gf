from pages.businesspage import businesspage
from util.config import host_port
import time


class TjcgxPage(businesspage):

    def __init__(self):
        businesspage.__init__(self)
        self.driver.get(f"http://{host_port}/water/#/buy/add")

    def get_shebeiclick(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > form > div:nth-child(1) > div:nth-child(1) > div > div > div > div > input')

    def get_phjcyclick(self):
        return self.driver.find_element_by_css_selector(
            'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(4) > span')

    def get_syrqclick(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > form > div:nth-child(2) > div:nth-child(1) > div > div > div > input')

    def get_syrqdayclick(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[4]/td[6]/div/span')

    def get_gmrqclick(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > form > div:nth-child(2) > div:nth-child(2) > div > div > div > input')

    def get_gmrqdayclick(self):
        return self.driver.find_element_by_css_selector(
            'body > div:nth-child(10) > div.el-picker-panel__body-wrapper > div > div.el-picker-panel__content > table.el-date-table > tbody > tr:nth-child(5) > td:nth-child(2) > div > span')

    def get_gmsl(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > form > div:nth-child(3) > div:nth-child(1) > div > div > div.el-input > input')

    def get_jineclick(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > form > div:nth-child(3) > div:nth-child(2) > div > div > div > input')

    def get_gmr(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > form > div:nth-child(4) > div > div > input')

    def get_ms(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > form > div:nth-child(5) > div > div > textarea')

    def get_ljcjclick(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > form > div:nth-child(6) > div > button.el-button.el-button--primary > span')

    def get_queding(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > div > div > div.el-dialog__footer > span > button.el-button.el-button--primary > span')

    def get_tjcgxwelcome(self):
        return self.driver.find_element_by_css_selector(
            'body > div.el-message.el-message--success > p')


class TjcgxCaozuo(TjcgxPage):

    def __init__(self):
        TjcgxPage.__init__(self)

    def click_shebei(self):
        self.get_shebeiclick().click()
        time.sleep(1)
    def click_phjcy(self):
        self.get_phjcyclick().click()

    def click_syrq(self):
        self.get_syrqclick().click()
        time.sleep(1)
    def click_syrqday(self):
        self.get_syrqdayclick().click()


    def click_gmrq(self):
        self.get_gmrqclick().click()
        time.sleep(1)

    def click_gmrqday(self):
        self.get_gmrqdayclick().click()

    def send_gmsl(self, gmsl):
        self.get_gmsl().send_keys(gmsl)

    def click_jine(self):
        self.get_jineclick().click()

    def send_gmr(self, gmr):
        self.get_gmr().send_keys(gmr)

    def send_ms(self, ms):
        self.get_ms().send_keys(ms)

    def click_ljcj(self):
        self.get_ljcjclick().click()

    def click_queding(self):
        self.get_queding().click()

    def text_tjcgx(self):
        return self.get_tjcgxwelcome().text


class TjcgxYewu(TjcgxCaozuo):

    def __init__(self):
        TjcgxCaozuo.__init__(self)

    def tjcgx_yewu(self, gmsl, gmr, ms):
        self.click_shebei()

        self.click_phjcy()

        self.click_syrq()

        self.click_syrqday()

        self.click_gmrq()

        self.click_gmrqday()

        self.send_gmsl(gmsl)

        self.click_jine()

        self.send_gmr(gmr)

        self.send_ms(ms)

        self.click_ljcj()

        self.click_queding()

        time.sleep(0.5)

        msg = self.text_tjcgx()
        print(msg)
        return msg


if __name__ == '__main__':
    TjcgxYewu().tjcgx_yewu(1, 2, 3)
