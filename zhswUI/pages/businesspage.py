# 后面的所有业务层必须要继承businessPage类
# 以后获取driver 和 一些公共的方法都写在这个类中

from WebDriver.get_fact import GetFact
from selenium.webdriver.support.ui import Select


class businesspage():

    def __init__(self):
        # 打开一个浏览器，将浏览器对象赋值给driver
        self.driver = GetFact.get_driver()

    # def alert_obj(self):
    #     a = self.driver.switch_to.alert
    #     a.text
    #     a.accept()

    # # 封装一个处理下拉选择框的方法
    # def clear_option(self, element, content):
    #     """
    #     :param element: 定位的下拉选择框
    #     :param content: 输入的选项文本
    #     """
    #     # Select() 里面接受的是定位到的下拉选择框
    #     s = Select(element)
    #     # 选择
    #     s.select_by_visible_text(content)