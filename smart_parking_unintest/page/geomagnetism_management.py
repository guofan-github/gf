# 页面元素定位层
import time

from selenium.webdriver.common.by import By

from webdriver.GetDriver import GetDriver


class GeomagnetismManagementPage(GetDriver):

    def __init__(self):
        self.driver = GetDriver.ger_driver()
        self.driver.get('http://192.168.163.131/smart_parking/#/equipment/WebGeomagnetism')
        # self.driver.get('http://192.168.163.131/smart_parking_bg/webRoad/roadName')
        time.sleep(2)

    # 新增按钮
    def get_geomagnetism_add(self):
        return self.wait_element_presence(By.XPATH,
                                          '//*[@id="app"]/section/section/main/div[3]/form/div[1]/button[3]/span')

    # 名字输入框
    def get_name_input(self):
        return self.wait_element_presence(By.XPATH,
                                          '//*[@id="app"]/section/section/main/div[3]/form/form/div[1]/div/div/input')

    # 编号输入框
    def get_id_input(self):
        return self.wait_element_presence(By.XPATH,
                                          '//*[@id="app"]/section/section/main/div[3]/form/form/div[2]/div/div/input')

    # 所属路段选择框
    def get_road_choose(self):
        return self.wait_element_presence(By.XPATH,
                                          '//*[@id="app"]/section/section/main/div[3]/form/div/div/div/div/div/input')

    # 路段
    def get_road(self):
        return self.wait_element_presence(By.XPATH,
                                          '//*[@role="tooltip"]/div[1]/div/div[1]/ul/li[2]/span')

    # 保存
    def get_save(self):
        return self.wait_element_presence(By.XPATH,
                                          '//*[@id="app"]/section/section/main/div[3]/form/button[1]/span')

    # 保存成功弹窗
    def get_alert(self):
        return self.wait_element_presence(By.XPATH,
                                          '//div[@class="el-notification__group"]/div/p')


# 操作层
class GeomagnetismManagementAction(GeomagnetismManagementPage):

    def __init__(self):
        GeomagnetismManagementPage.__init__(self)

    # 点击新增按钮
    def click_add(self):
        self.get_geomagnetism_add().click()
        time.sleep(2)

    # 输入名字
    def input_name(self, name):
        self.get_name_input().send_keys(name)
        # time.sleep(1)

    # 输入编号
    def input_id(self, id):
        self.get_id_input().send_keys(id)
        # time.sleep(1)

    # 点击路段选择框
    def click_road_choose(self):
        self.get_road_choose().click()
        time.sleep(2)

    # 选择路段
    def click_road(self):
        self.get_road().click()
        time.sleep(1)

    # 点击保存
    def click_save(self):
        self.get_save().click()
        time.sleep(1.5)

    # 保存成功弹窗文本
    def get_alert_text(self):
        return self.get_alert().text


# 业务层
class GeomagnetismManagementBusiness(GeomagnetismManagementAction):

    def __init__(self):
        GeomagnetismManagementAction.__init__(self)

    # 新增地磁
    def add_geomagnetism(self, name, id):
        # 点击新增
        self.click_add()
        # 输入名字
        self.input_name(name)
        # 输入id
        self.input_id(id)
        # 点击路段选择框
        self.click_road_choose()
        # 点击路段
        self.click_road()
        # 点击保存
        self.click_save()
        msg = self.get_alert_text()
        return msg


# 删除测试数据
class DelTestData(GetDriver):

    def __init__(self):
        pass

    def del_data(self):
        el = self.wait_element_presence(By.XPATH,
                                        '/html/body/div[1]/section/section/main/div[3]/form/div[2]/div['
                                        '3]/table/tbody/tr[ '
                                        '1]/td[9]/div/button[1]')
        el.click()
        time.sleep(3)

        alert = self.wait_element_presence(By.XPATH,
                                           '//div[@class="el-message-box__btns"]/button[2]/span')
        alert.click()
