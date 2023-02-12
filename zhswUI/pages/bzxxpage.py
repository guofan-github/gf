import time



# 页面定位层
from pages.businesspage import businesspage
from util.config import host_port


class bzxxpage(businesspage):
    def __init__(self):
        businesspage.__init__(self)
        # 进入页面
        self.driver.get(f'http://{host_port}/water/#/gms/pump')
        time.sleep(2)
    # 添加
    def get_bzxx_tianjia(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/form/div[4]/div/button[3]/span')

    # 名称
    def get_bzxx_mingcheng(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/input')

    # 型号
    def get_bzxx_xinghao(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[4]/div/div[2]/form/div[1]/div[2]/div/div/div/input')

    # 确认添加
    def get_bzxx_qrtianjia(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[4]/div/div[3]/div/button[2]/span')

    # 添加弹窗
    def get_bzxx_tjtc(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

    # 修改
    def get_bzxx_xiugai(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[11]/div/button[1]/span')

    # 泵站信息
    def get_bzxx_xinxi(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[1]/div[1]/div/div/div/input')

    # 泵站类型
    def get_bzxx_leixing(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[2]/form/div[5]/div/div/input')

    # 确定
    def get_bzxx_queding(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[3]/div/button[2]/span')

    # 修改弹窗
    def get_bzxx_xgtc(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

    # 删除
    def get_bzxx_shanchu(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[11]/div/button[2]/span')

    # 删除弹窗
    def get_bzxx_sctc(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

# 操作层
class bzxxcaozuo(bzxxpage):

    def __init__(self):
        bzxxpage.__init__(self)
    # 点击添加
    def click_bzxx_tianjia(self):
        self.get_bzxx_tianjia().click()
        time.sleep(1)

    # 输入名称
    def send_bzxx_mingcheng(self):
        self.get_bzxx_mingcheng().clear()
        self.get_bzxx_mingcheng().send_keys('卢本伟')

    # 输入型号
    def send_bzxx_xinghao(self):
        self.get_bzxx_xinghao().clear()
        self.get_bzxx_xinghao().send_keys('特别型')

    # 点击确定
    def click_bzxx_qdtianjia(self):
        self.get_bzxx_qrtianjia().click()
        time.sleep(0.5)

    # 获取弹窗
    def get_bzxx_tjtctext(self):
        return self.get_bzxx_tjtc().text

    # 点击修改
    def click_bzxx_xiugai(self):
        self.get_bzxx_xiugai().click()
        time.sleep(1)

    # 输入泵站信息
    def send_bzxx_xinxi(self):
        self.get_bzxx_xinxi().send_keys('卢本伟广场泵站')

    # 输入泵站类型
    def send_bzxx_leixing(self):
        self.get_bzxx_leixing().send_keys('三四层楼那么高')

    # 点击确定
    def click_bzxx_queding(self):
        self.get_bzxx_queding().click()
        time.sleep(0.5)

    # 获取修改成功弹窗
    def get_bzxx_xjtctext(self):
        return self.get_bzxx_xgtc().text

    # 点击删除
    def click_bzxx_shanchu(self):
        self.get_bzxx_shanchu().click()
        time.sleep(1)

    # 获取删除成功文本
    def get_bzxx_sctctext(self):
        return self.get_bzxx_sctc().text

# 业务层
class bzxxyewu(bzxxcaozuo):

    def __init__(self):
        bzxxcaozuo.__init__(self)

    # 添加
    def bzxx_tianjia(self):
        # 点击添加
        self.click_bzxx_tianjia()
        # 输入名称
        self.send_bzxx_mingcheng()
        # 输入型号
        self.send_bzxx_xinghao()
        # 点击确定
        self.click_bzxx_qdtianjia()
        msg = self.get_bzxx_tjtctext()
        print(msg)
        return msg

    # 修改
    def bzxx_xiugai(self):
        # 点击修改
        self.click_bzxx_xiugai()
        # 输入信息
        self.send_bzxx_xinxi()
        # 输入类型
        self.send_bzxx_leixing()
        # 点击确定
        self.click_bzxx_queding()
        # 获取文本
        msg = self.get_bzxx_xjtctext()
        print(msg)
        return msg

    # 删除
    def bzxx_shanchu(self):
        # 点击删除
        self.click_bzxx_shanchu()
        # 获取删除文本
        msg = self.get_bzxx_sctctext()
        return msg

if __name__ == '__main__':
    bzxxyewu().bzxx_tianjia()
