import time

# 页面元素定位
from pages.businesspage import businesspage
from util.config import host_port


class sblbpage(businesspage):

    def __init__(self):
        businesspage.__init__(self)
        # 进入页面
        self.driver.get(f"http://{host_port}/water/#/device/list")
        time.sleep(3)

    # 分配设备定位
    def get_sblb_fpsb(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[2]/div/div/button[1]/span')

    # 选择设施框
    def get_sblb_xzssk(self):
        return self.driver.find_element_by_xpath('//div[@class="el-cascader"]//input')

    # 选择公司
    def get_sblb_xzgs(self):
        return self.driver.find_element_by_xpath('//div[@x-placement="bottom-start"]//span')

    # 选择设施点
    def get_sblb_xzssd(self):
        return self.driver.find_element_by_xpath('//div[@class="el-cascader-panel"]/div[2]/div/ul/li/span')

    # 选择设施
    def get_sblb_xzss(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/ul/li[1]/span')

    # 设备选择框
    def get_sblb_sbxzk(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[8]/div/div[2]/form/div[2]/div/div/div/div/div/input')

    # 选择设备
    def get_sblb_xzsb(self):
        return self.driver.find_element_by_xpath('//div[@class="el-scrollbar"]/div/ul/li[1]/span')

    # 输入分配数量
    def get_sblb_shurushuliang(self):
        return self.driver.find_element_by_css_selector('input[placeholder="请输入分配该设备的数量"]')

    # 分配按钮
    def get_sblb_fenpeianniu(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[8]/div/div[3]/div/button[2]/span')

    # 分配成功弹窗
    def get_sblb_fptanchuang(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

    # 待批列表
    def get_sblb_dplb(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[2]/div/div/span[1]/span/button/span')

    # 批复
    def get_sblb_pifu(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[5]/div[2]/table/tbody/tr[3]/td[6]/div/button/span')

    # 输入批复数量
    def get_sblb_pifushuliang(self):
        return self.driver.find_element_by_css_selector('input[placeholder="请输入批复数量"]')

    # 输入说明
    def get_sblb_pifushuoming(self):
        return self.driver.find_element_by_css_selector('textarea[placeholder="请输入回复说明"]')

    # 批复按钮
    def get_sblb_pifuanniu(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[6]/div/div[3]/div/button[2]/span')

    # 批复成功弹窗
    def get_sblb_pftanchuang(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/p')

    # 修改
    def get_sblb_xiugai(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[3]/div/div[5]/div[2]/table/tbody/tr[1]/td[11]/div/button[2]/span')

    # 修改设备型号
    def get_sblb_xjsbxh(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[7]/div/div[2]/form/div[1]/div[1]/div/div/div/input')

    # 修改设备名称
    def get_sblb_xjsbmc(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[7]/div/div[2]/form/div[1]/div[2]/div/div/div/input')

    # 修改单价
    def get_sblb_danjia(self):
        return self.driver.find_element_by_css_selector('input[placeholder="请输入采购单价"]')

    # 修改数量
    def get_sblb_xjshuliang(self):
        return self.driver.find_element_by_css_selector('input[placeholder="请输入采购数量"]')

    # 修改按钮
    def get_sblb_xiugaianniu(self):
        return self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div[3]/div[7]/div/div[3]/div/button[2]/span')

    # 修改成功弹窗
    def get_sblb_xiugaitanchuang(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')


# 操作层
class sblbcaozuo(sblbpage):

    def __init__(self):
        sblbpage.__init__(self)

    # 点击分配设备
    def click_sblb_fpsb(self):
        self.get_sblb_fpsb().click()
        time.sleep(1)

    # 点击设施框
    def click_sblb_sheshik(self):
        self.get_sblb_xzssk().click()
        time.sleep(1)

    # 点击公司
    def click_sblb_sbgs(self):
        self.get_sblb_xzgs().click()
        time.sleep(1)

    # 点击设施点
    def click_sblb_sheshid(self):
        self.get_sblb_xzssd().click()
        time.sleep(1)

    # 点击设施
    def click_sblb_sheshi(self):
        self.get_sblb_xzss().click()

    # 点击设备框
    def click_sblb_shebeik(self):
        self.get_sblb_sbxzk().click()
        time.sleep(1)

    # 点击设备
    def click_sblb_shebei(self):
        self.get_sblb_xzsb().click()
        time.sleep(1)

    # 输入分配数量
    def send_sblb_fpshuliang(self):
        self.get_sblb_shurushuliang().send_keys('1')

    # 点击分配
    def click_sblb_fpanniu(self):
        self.get_sblb_fenpeianniu().click()
        time.sleep(0.5)

    # 获取分配弹窗文本
    def get_sblb_tctext(self):
        return self.get_sblb_fptanchuang().text

    # 点击待批列表
    def click_sblb_dplb(self):
        self.get_sblb_dplb().click()
        time.sleep(3)

    # 点击批复
    def click_sblb_pf(self):
        self.get_sblb_pifu().click()
        time.sleep(1)

    # 输入批复数量
    def send_sblb_pfshuliang(self):
        self.get_sblb_pifushuliang().send_keys('1')

    # 输入说明
    def send_sblb_pfsm(self):
        self.get_sblb_pifushuoming().send_keys('批了，我指甲批了')

    # 点击批复按钮
    def click_sblb_pifuanniu(self):
        self.get_sblb_pifuanniu().click()

    # 获取批复成功弹窗
    def get_sblb_pftext(self):
        return self.get_sblb_pftanchuang().text

    # 点击修改
    def click_sblb_xiugai(self):
        self.get_sblb_xiugai().click()
        time.sleep(1)

    # 输入设备型号
    def send_sblb_xjsbxh(self):
        self.get_sblb_xjsbxh().clear()
        self.get_sblb_xjsbxh().send_keys('苹果')

    # 输入设备名称
    def send_sblb_xjsbmc(self):
        self.get_sblb_xjsbmc().clear()
        self.get_sblb_xjsbmc().send_keys('苹果99 Pro')

    # 输入单价
    def send_sblb_xjdj(self):
        self.get_sblb_danjia().clear()
        self.get_sblb_danjia().send_keys('10')

    # 输入数量
    def send_sblb_xjsl(self):
        self.get_sblb_xjshuliang().send_keys('1')

    # 点击修改按钮
    def click_sblb_xiugaianniu(self):
        self.get_sblb_xiugaianniu().click()
        time.sleep(0.5)

    # 获取弹窗文本
    def get_sblb_xjtext(self):
        return self.get_sblb_xiugaitanchuang().text


# 业务层
class sblbyewu(sblbcaozuo):

    def __init__(self):
        sblbcaozuo.__init__(self)

    # 分配设备
    def sblb_fpsb(self):
        # 点击分配设备
        self.click_sblb_fpsb()
        # 点击设施框
        self.click_sblb_sheshik()
        # 点击公司
        self.click_sblb_sbgs()
        # 点击设施点
        self.click_sblb_sheshid()
        # 点击设施
        self.click_sblb_sheshi()
        # 点击设备框
        self.click_sblb_shebeik()
        # 点击设备
        self.click_sblb_shebei()
        # 输入分配数量
        self.send_sblb_fpshuliang()
        # 点击分配
        self.click_sblb_fpanniu()
        # 获取分配弹窗文本
        msg = self.get_sblb_tctext()

        return msg

    # 待批列表
    def sblb_dplb(self):
        # 点击待批列表
        self.click_sblb_dplb()
        # 点击批复
        self.click_sblb_pf()
        # 输入批复数量
        self.send_sblb_pfshuliang()
        # 输入说明
        self.send_sblb_pfsm()
        # 点击批复按钮
        self.click_sblb_pifuanniu()
        msg = self.get_sblb_pftext()
        return msg

    # 修改
    def sblb_xiugai(self):
        # 点击修改
        self.click_sblb_xiugai()
        # 输入设备型号
        self.send_sblb_xjsbxh()
        # 输入设备名称
        self.send_sblb_xjsbmc()
        # 输入单价
        self.send_sblb_xjdj()
        # 输入数量
        self.send_sblb_xjsl()
        # 点击修改按钮
        self.click_sblb_xiugaianniu()
        # 获取弹窗文本
        msg = self.get_sblb_xjtext()
        return msg


if __name__ == '__main__':
    sblbyewu().sblb_dplb()
