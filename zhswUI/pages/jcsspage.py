import time






# 页面元素定位层
from pages.businesspage import businesspage
from util.config import host_port


class jcsspage(businesspage):

    def __init__(self):
        businesspage.__init__(self)
        # 进入页面
        self.driver.get(f"http://{host_port}/water/#/property/8")
        time.sleep(3)

    # 新增按钮
    def get_jcss_xinzeng(self):
        return self.driver.find_element_by_xpath('//div[@class="grid-content"]/button')

    # 定位设施编号
    def get_jcss_ssbianhao(self):
        return self.driver.find_element_by_xpath('//div[@class="el-dialog__body"]//div[@class="el-cascader"]//input')

    # 定位公司
    def get_jcss_ssgs(self):
        return self.driver.find_element_by_xpath('//div[@class="el-popper el-cascader__dropdown"]//li[1]/i')
    # 定位设施编号选择 二次供水设备
    def get_jcss_ssbianhaoxuanze(self):
        return self.driver.find_element_by_xpath('//div[@class="el-cascader-panel"]/div[2]/div/ul/li[3]/span')

    # 定位新增名称
    def get_jcss_ssname(self):
        return self.driver.find_element_by_css_selector('input[placeholder="请输入新增名称"]')

    # 定位选择日期
    def get_jcss_ssdate(self):
        return self.driver.find_element_by_css_selector('input[placeholder="选择日期"]')

    # 定位具体日期 2022.6.23
    def get_jcss_ssdatexuanze(self):
        return self.driver.find_element_by_xpath('//table[@class="el-date-table"]//tr[5]/td[5]')

    # 定位经度
    def get_jcss_ssjingdu(self):
        return self.driver.find_element_by_css_selector('input[placeholder="请输入经度"]')

    # 定位纬度
    def get_jcss_ssweidu(self):
        return self.driver.find_element_by_css_selector('input[placeholder="请输入纬度"]')

    # 定位地址
    def get_jcss_ssdizhi(self):
        return self.driver.find_element_by_css_selector('input[placeholder="请输入设施地址"]')

    # 定位描述
    def get_jcss_ssmiaoshu(self):
        return self.driver.find_element_by_css_selector('textarea[placeholder="请输入描述"]')

    # 定位添加按钮
    def get_jcss_sstianjia(self):
        return self.driver.find_element_by_xpath('//div[@class="el-dialog__footer"]//button[2]')
    # 弹窗定位
    def get_jcss_tanchuan(self):
        return self.driver.find_element_by_css_selector('p[class="el-message__content"]')

    # 详情定位
    def get_jcss_xiangqing(self):
        return self.driver.find_element_by_xpath('//table/tbody/tr[1]/td[5]/div/button/span')

    # 申请定位
    def get_jcss_shenqing(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/section/section/main/div/div[2]/div/div[2]/div[2]/div/div/section/div[4]/div/button[2]')

    # 申请理由
    def get_jcss_liyou(self):
        return self.driver.find_element_by_css_selector('input[placeholder="请填写设备申请理由"]')

    # 申请数量
    def get_jcss_shuliang(self):
        return self.driver.find_element_by_css_selector('input[placeholder="请填写申请数量"]')

    # 确认申请
    def get_jcss_shenqinganniu(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/section/section/main/div/div[2]/div/div[2]/div[5]/div/div[3]/div/button[2]/span')

    # 申请成功弹窗
    def get_jcss_sqtanchuang(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

# 操作层
class jcsscaozuo(jcsspage):

    def __init__(self):
        jcsspage.__init__(self)

    # 点击新增按钮
    def click_jcss_ssxz(self):
        self.get_jcss_xinzeng().click()
        time.sleep(1)

    # 点击设施编号
    def click_jcss_ssbh(self):
        self.get_jcss_ssbianhao().click()
        time.sleep(1)
    # 点击公司
    def click_jcss_ssgs(self):
        self.get_jcss_ssgs().click()
        time.sleep(1)
    # 点击二次供水设备
    def click_jcss_ssbhxz(self):
        self.get_jcss_ssbianhaoxuanze().click()
        time.sleep(1)

    # 输入名称
    def send_jcss_ssname(self):
        self.get_jcss_ssname().send_keys('lbw')

    # 点击日期选择
    def click_jcss_data(self):
        self.get_jcss_ssdate().click()
        time.sleep(1)

    # 具体日期选择 23号
    def click_jcss_dataxuanze(self):
        self.get_jcss_ssdatexuanze().click()
        time.sleep(1)

    # 经度输入
    def send_jcss_ssjd(self):
        self.get_jcss_ssjingdu().send_keys('88')

    # 纬度输入
    def send_jcss_sswd(self):
        self.get_jcss_ssweidu().send_keys('88')

    # 地址输入
    def send_jcss_dizhi(self):
        self.get_jcss_ssdizhi().send_keys('卢本伟广场')

    # 描述输入
    def send_jcss_miaoshu(self):
        self.get_jcss_ssmiaoshu().send_keys('从现在开始，这里叫做卢本伟广场')
        time.sleep(1)

    # 点击添加按钮
    def click_jcss_tianjia(self):
        self.get_jcss_sstianjia().click()
        time.sleep(1)
    # 获取弹窗文本
    def get_jcss_text(self):
        return self.get_jcss_tanchuan().text

    # 点击详情
    def click_jcss_xiangqing(self):
        self.get_jcss_xiangqing().click()
        time.sleep(1)
    # 点击申请
    def click_jcss_shenqing(self):
        self.get_jcss_shenqing().click()
        time.sleep(1)

    # 输入申请理由
    def send_jcss_liyou(self):
        self.get_jcss_liyou().send_keys('没钱了，申请几台机器卖了换点钱')

    # 输入申请数量
    def send_jcss_shuliang(self):
        self.get_jcss_shuliang().send_keys('66')

    # 点击确认申请
    def click_jcss_shenqinganniu(self):
        self.get_jcss_shenqinganniu().click()
        time.sleep(1)

    # 获取申请成功弹窗文本
    def get_jcss_tanchuangtext(self):
        return self.get_jcss_sqtanchuang().text

# 业务层
class jcssyewu(jcsscaozuo):

    def __init__(self):
        jcsscaozuo.__init__(self)

    # 设施新增
    def jcss_sheshi(self):
        # 点击新增
        self.click_jcss_ssxz()
        # 选择设施编号
        self.click_jcss_ssbh()
        self.click_jcss_ssgs()
        self.click_jcss_ssbhxz()
        # 输入名称
        self.send_jcss_ssname()
        # 选择日期
        self.click_jcss_data()
        self.click_jcss_dataxuanze()
        # 经度输入
        self.send_jcss_ssjd()
        # 纬度输入
        self.send_jcss_sswd()
        # 地址输入
        self.send_jcss_dizhi()
        # 描述输入
        self.send_jcss_miaoshu()
        # 点击添加按钮
        self.click_jcss_tianjia()
        # 获取弹窗文本
        msg = self.get_jcss_text()

        return msg

    # 申请设施
    def jcss_shenqing(self):
        # 点击详情
        self.click_jcss_xiangqing()
        # 点击申请
        self.click_jcss_shenqing()
        # 输入理由
        self.send_jcss_liyou()
        # 输入数量
        self.send_jcss_shuliang()
        # 确认申请
        self.click_jcss_shenqinganniu()
        # 获取弹窗文本
        msg = self.get_jcss_tanchuangtext()

        return msg