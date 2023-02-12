import time



# 元素定位层
from pages.businesspage import businesspage
from util.config import host_port


class dtdwpage(businesspage):

    def __init__(self):
        businesspage.__init__(self)
        # 进入页面
        self.driver.get(f'http://{host_port}/water/#/gms/map')
        time.sleep(2)

    # 地图
    def get_dtdw_ditu(self):
        return self.driver.find_element_by_id('mask')

    # 泵站数据信息
    def get_dtdw_xinxi(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[2]/div/div[2]/button[2]/span')

    # 弹窗
    def get_dtdw_tc(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[2]/div/div[1]/span')


    # X
    def get_dtdw_X(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[2]/div/div[1]/button/i')

# 操作层
class dtdwcaozuo(dtdwpage):

    def __init__(self):
        dtdwpage.__init__(self)

    # 点击地图
    def click_dtdw_ditu(self):
        self.get_dtdw_ditu().click()
        time.sleep(1)

    # 点击信息
    def click_dtdw_xinxi(self):
        self.get_dtdw_xinxi().click()

    # 获取文本
    def get_dtdw_tctext(self):
        return self.get_dtdw_tc().text

    # 点击X
    def click_dtdw_X(self):
        self.get_dtdw_X().click()

class dtdwyewu(dtdwcaozuo):

    def __init__(self):
        dtdwcaozuo.__init__(self)

    # 看泵站信息
    def dtdw_ditu(self):
        # 点击地图
        self.click_dtdw_ditu()
        # 点击信息
        self.click_dtdw_xinxi()
        # 获取文本
        msg = self.get_dtdw_tctext()
        # 点X
        self.click_dtdw_X()
        return msg

if __name__ == '__main__':
    dtdwyewu().dtdw_ditu()