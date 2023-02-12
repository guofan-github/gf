from pages.businesspage import businesspage
from util.config import host_port
import time


# 页面元素定位层
class xjddpage(businesspage):

    def __init__(self):
        businesspage.__init__(self)
        # 进入页面
        self.driver.get(f"http://{host_port}/water/#/patrol/item")
        time.sleep(3)

    # 定位 添加 按钮
    def get_xjdd_tianjia(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > button > span')

    # 定位 巡检地点编号
    def get_xjdd_bianhao(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > div:nth-child(6) > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div > input')

    # 定位 巡检地点名称
    def get_xjdd_mingcheng(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > div:nth-child(6) > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div > input')

    # 定位 巡检地点地址
    def get_xjdd_dizhi(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > div:nth-child(6) > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > input')

    # 定位 巡检地点备注
    def get_xjdd_beizhu(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > div:nth-child(6) > div > div.el-dialog__body > form > div:nth-child(4) > div > div > div > textarea')

    # 定位 最后确定【添加】按钮
    def get_xjdd_zuihoutianjia(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > div:nth-child(6) > div > div.el-dialog__footer > div > button.el-button.el-button--primary > span')

    #翻页
    def get_xjdd_fanye(self):
        return self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[3]/div[3]/button[2]/i')

    # 定位 修改 按钮
    def get_xjdd_xiugai(self):
        return self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[3]/div[2]/div/div[3]/table/tbody/tr/td[6]/div/button[1]/span')

    # 定位 修改 巡检地点编号
    def get_xjdd_xgbianhao(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > div:nth-child(7) > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div > input')

    # 定位 修改 巡检地点名称
    def get_xjdd_xgmingcheng(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > div:nth-child(7) > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > div > input')

    # 定位 修改 巡检地点地址
    def get_xjdd_xgdizhi(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > div:nth-child(7) > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > input')

    # 定位 修改 巡检地点备注
    def get_xjdd_xgbeizhu(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > div:nth-child(7) > div > div.el-dialog__body > form > div:nth-child(4) > div > div > div > textarea')

    # 定位 最后确定【修改】按钮
    def get_xjdd_zuihouxiugai(self):
        return self.driver.find_element_by_css_selector(
            '#app > section > section > main > div:nth-child(3) > div:nth-child(7) > div > div.el-dialog__footer > div > button.el-button.el-button--primary > span')

    # 定位 删除 按钮
    def get_xjdd_shanchu(self):
        return self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[3]/div[2]/div/div[3]/table/tbody/tr/td[6]/div/button[2]/span')

    # 定位 删除 确定
    def get_xjdd_shanchuqueding(self):
        return self.driver.find_element_by_css_selector(
            'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span')

    # 定位 删除成功
    def get_xjdd_shanchuchenggong(self):
        return self.driver.find_element_by_css_selector(
            'body > div.el-message.el-message--info > p')


# 操作层
class xjddcaozuo(xjddpage):

    def __init__(self):
        xjddpage.__init__(self)

    def click_tianjia(self):
        self.get_xjdd_tianjia().click()
        time.sleep(2)

    def send_bianhao(self, bianhao):
        self.get_xjdd_bianhao().send_keys(bianhao)

    def send_mingcheng(self, mingcheng):
        self.get_xjdd_mingcheng().send_keys(mingcheng)

    def send_dizhi(self, dizhi):
        self.get_xjdd_dizhi().send_keys(dizhi)

    def send_beizhu(self, beizhu):
        self.get_xjdd_beizhu().send_keys(beizhu)

    def click_zuihoutianjia(self):
        self.get_xjdd_zuihoutianjia().click()

    def click_fanye(self):
        self.get_xjdd_fanye().click()

    def click_xiugai(self):
        self.get_xjdd_xiugai().click()

    def send_xgbianhao(self, xgbianhao):
        self.get_xjdd_xgbianhao().clear()
        self.get_xjdd_xgbianhao().send_keys(xgbianhao)

    def send_xgmingcheng(self, xgmingcheng):
        self.get_xjdd_xgmingcheng().clear()
        self.get_xjdd_xgmingcheng().send_keys(xgmingcheng)

    def send_xgdizhi(self, xgdizhi):
        self.get_xjdd_xgdizhi().clear()
        self.get_xjdd_xgdizhi().send_keys(xgdizhi)

    def send_xgbeizhu(self, xgbeizhu):
        self.get_xjdd_xgbeizhu().clear()
        self.get_xjdd_xgbeizhu().send_keys(xgbeizhu)

    def click_zuihouxiugai(self):
        self.get_xjdd_zuihouxiugai().click()

    def click_shanchu(self):
        self.get_xjdd_shanchu().click()

    def click_shanchuqueding(self):
        self.get_xjdd_shanchuqueding().click()

    def get_shanchuchenggongtext(self):
        print(self.get_xjdd_shanchuchenggong().text)
        return self.get_xjdd_shanchuchenggong().text





# 业务层
class xjddyewu(xjddcaozuo):

    def __init__(self):
        xjddcaozuo.__init__(self)

    # 新增员工
    def xjdd_yewu(self, bianhao, mingcheng, dizhi, beizhu, xgbianhao, xgmingcheng, xgdizhi, xgbeizhu):


        self.click_tianjia()

        self.send_bianhao(bianhao)

        self.send_mingcheng(mingcheng)

        self.send_dizhi(dizhi)

        self.send_beizhu(beizhu)

        self.click_zuihoutianjia()
        self.click_fanye()
        time.sleep(3)

        self.click_xiugai()

        self.send_xgbianhao(xgbianhao)

        self.send_xgmingcheng(xgmingcheng)

        self.send_xgdizhi(xgdizhi)

        self.send_xgbeizhu(xgbeizhu)

        self.click_zuihouxiugai()
        time.sleep(3)

        self.click_shanchu()

        self.click_shanchuqueding()
        time.sleep(3)
        msg = self.get_shanchuchenggongtext()

        return msg
