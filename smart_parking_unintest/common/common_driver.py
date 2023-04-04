from selenium.webdriver.support.wait import WebDriverWait

from webdriver.GetDriver import GetDriver


class CommonDriver:

    def __init__(self):
        self.driver = GetDriver.ger_driver()


    @classmethod
    def wait_element_presence(cls, by, value, time_out = 5):
        return WebDriverWait(cls.driver)