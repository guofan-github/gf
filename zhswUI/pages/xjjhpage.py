import time
from WebDriver.get_fact import GetFact
from util.config import host_port
from pages.businesspage import businesspage

# 元素定位层

class xjjhpage(businesspage):
    def __init__(self):
        businesspage.__init__(self)
        self.driver.get(f'http://{host_port}/water/#/patrol/plan')
        time.sleep(2)


    # 查看
    def get_xjjh_chakan(self):
        return self.driver.find_element_by_xpath('//tbody/tr[1]/td[9]//button[1]')
    # 查看-确定
    def get_xjjh_ckqd(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[5]/div/div[3]/div/button')


    # 添加
    def get_xjjh_tianjia(self):
        return self.driver.find_element_by_xpath('//button[@class="el-button btn1 el-button--success is-plain"]/span')
# 添加巡检计划元素定位
    # 巡检编号
    def get_xjjh_xjbh(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div[1]/input')
    # 计划名称
    def get_xjjh_jhmc(self):
        return self.driver.find_element_by_xpath('//div[@class="el-col el-col-10 el-col-push-1"]//input[@placeholder="请输入计划名称"]')
    # 巡检类型
    def get_xjjh_xjlx(self):
        return self.driver.find_element_by_xpath('//div[2]/div[1]/div/div/div/div/input')
    # 巡检类型-下拉框
    def get_xjjh_xjlxxlk(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]')
    # 巡检周期
    def get_xjjh_xjzq(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[4]/div/div[2]/form/div[2]/div[2]/div/div/div/div[1]/input')
    # 巡检周期-下拉框
    def get_xjjh_xjzqxlk(self):
        return self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')
    # 开始日期
    def get_xjjh_kaishiriqi(self):
        return self.driver.find_element_by_xpath('//form/div[3]/div[1]/div/div/div/input')
    # 开始日期-下拉框
    def get_xjjh_ksrqxlk(self):
        return self.driver.find_element_by_xpath('//div[1]/div/div[2]/table[1]/tbody/tr[2]/td[4]/div/span')
    # 结束日期
    def get_xjjh_jieshuriqi(self):
        return self.driver.find_element_by_xpath('//form/div[3]/div[2]/div/div/div[1]/input')
    # 结束日期-下拉框
    def get_xjjh_jsrqxlk(self):
        return self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[5]/div/span')
    # 备注
    def get_xjjh_beizhu(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div[3]/div[4]/div/div[2]/form/div[4]/div/div/div/div/textarea')
    # 勾选 请选择添加巡检点
    def get_xjjh_gouxuanjjdd(self):
        return self.driver.find_element_by_xpath('//tr[5]/td[1]/div/label/span/span')
    # 【添加】按钮
    def get_xjjh_tianjiaanniu(self):
        return self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[3]/div[4]/div/div[3]/div/button[2]/span')
    # 【取消】按钮
    # def get_xjjh_quxiaoanniu(self):
    #     return self.driver.find_element_by_xpath('//div[3]/div[4]/div/div[3]/div/button[1]/span')

    # 添加成功后【添加成功】断言
    def get_xjjh_tjdy(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

    # 修改
    def get_xjjh_xiugai(self):
        return self.driver.find_element_by_xpath('//tbody/tr[1]/td[9]//button[2]')
# 修改巡检计划
    # 巡检编号
    def get_xjjh_xjxjbh(self):
        return self.driver.find_element_by_xpath('//div[6]/div/div[2]/form/div[1]/div[1]/div/div/div/input')
    # 计划名称
    def get_xjjh_xjjhmc(self):
        return self.driver.find_element_by_xpath('//div[6]/div/div[2]/form/div[1]/div[2]/div/div/div/input')
    # 巡检类型
    def get_xjjh_xjxjlx(self):
        return self.driver.find_element_by_xpath('//div[6]/div/div[2]/form/div[2]/div[1]/div/div/div/div[1]/input')
    # 巡检类型-下拉框
    def get_xjjh_xjxjlxxlk(self):
        return self.driver.find_element_by_xpath('//div[8]/div[1]/div[1]/ul/li[2]/span')
    # 巡检周期
    def get_xjjh_xjxjzq(self):
        return self.driver.find_element_by_xpath('//div[6]/div/div[2]/form/div[2]/div[2]/div/div/div/div/input')
    # 巡检周期-下拉框
    def get_xjjh_xjxjzqxlk(self):
        return self.driver.find_element_by_xpath('/html/body/div[8]/div[1]/div[1]/ul/li[4]')
    # 开始日期
    def get_xjjh_xjkaishiriqi(self):
        return self.driver.find_element_by_xpath('//div[6]/div/div[2]/form/div[3]/div[1]/div/div/div/input')
    # 开始日期-下拉框
    def get_xjjh_xjksrqxlk(self):
        return self.driver.find_element_by_xpath('/html/body/div[8]/div[1]/div/div[2]/table[1]/tbody/tr[2]/td[4]/div/span')
    # 结束日期
    def get_xjjh_xjjieshuriqi(self):
        return self.driver.find_element_by_xpath('//div[6]/div/div[2]/form/div[3]/div[2]/div/div/div/input')
    # 结束日期-下拉框
    def get_xjjh_xjjsrqxlk(self):
        return self.driver.find_element_by_xpath('/html/body/div[9]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[1]/div/span')
    # 备注
    def get_xjjh_xjbeizhu(self):
        return self.driver.find_element_by_xpath('//div[6]/div/div[2]/form/div[4]/div/div/div/div/textarea')
    # 勾选 请选择修改巡检点
    def get_xjjh_xjgouxuanjjdd(self):
        return self.driver.find_element_by_xpath('//div[6]/div/div[2]/form/div[6]/div/div/div[3]/table/tbody/tr[4]/td[1]/div/label/span/span')
    # 【修改】按钮
    def get_xjjh_xjtianjiaanniu(self):
        return self.driver.find_element_by_xpath('//div[6]/div/div[3]/div/button[2]/span')


    # 修改成功后【修改成功】断言
    def get_xjjh_xgcg(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"]//p')

    # # 【取消】按钮
    # def get_xjjh_xjquxiaoanniu(self):
    #     return self.driver.find_element_by_xpath('//div[6]/div/div[3]/div/button[1]/span')


    # 删除
    def get_xjjh_shanchu(self):
        return self.driver.find_element_by_xpath('//tbody/tr[1]/td[9]//button[3]')
    # 提示【确定】删除
    def get_xjjh_xjshanchu(self):
        return self.driver.find_element_by_xpath('//div[@class="el-message-box__btns"]//button[2]/span')

    # 删除失败后【删除失败】断言
    def get_xjjh_scsb(self):
        return self.driver.find_element_by_xpath('//div[@class="el-message el-message--info"]//p')

# 操作层
class xjjhcaocuo(xjjhpage):
    def __init__(self):
        xjjhpage.__init__(self)
    # 添加
    def send_xjjh_tianjia(self):
        self.get_xjjh_tianjia().click()
    # 查看
    def send_xjjh_chakan(self):
        self.get_xjjh_chakan().click()
    # 修改
    def send_xjjh_xiugai(self):
        self.get_xjjh_xiugai().click()
    # 删除
    def send_xjjh_shanchu(self):
        self.get_xjjh_shanchu().click()
        time.sleep(1)
    # 提示【确定】删除
    def send_xjjh_xjshanchu(self):
        self.get_xjjh_xjshanchu().click()

    # 删除失败后【删除失败】断言
    def get_xjjh_xjscsb(self):
        return self.get_xjjh_scsb().text



# 添加巡检计划操作层
    # 添加-巡检编号
    def send_xjjh_xjbh(self,xjbh):
        self.get_xjjh_xjbh().send_keys(xjbh)
    # 添加-计划名称
    def send_xjjh_jhmc(self,jhmc):
        self.get_xjjh_jhmc().send_keys(jhmc)
    # 添加-巡检类型
    def send_xjjh_xjlx(self):
        self.get_xjjh_xjlx().click()
        time.sleep(2)

    #添加-巡检类型-下拉框
    def send_xjjh_xjlxxlk(self):

        self.get_xjjh_xjlxxlk().click()
        time.sleep(1)

    # 巡检周期
    def send_xjjh_xjzq(self):

        self.get_xjjh_xjzq().click()
        time.sleep(2)
    # 巡检周期-下拉框
    def send_xjjh_xjzqxlk(self):
        self.get_xjjh_xjzqxlk().click()
        time.sleep(2)
    # 开始日期
    def send_xjjh_kaishiriqi(self):
        self.get_xjjh_kaishiriqi().click()
        time.sleep(2)
    # 开始日期-下拉框
    def send_xjjh_ksrqxlk(self):
        self.get_xjjh_ksrqxlk().click()
        time.sleep(2)
    # 结束日期
    def send_xjjh_jieshuriqi(self):
        self.get_xjjh_jieshuriqi().click()
        time.sleep(2)
    # 结束日期-下拉框
    def send_xjjh_jsrqxlk(self):
        self.get_xjjh_jsrqxlk().click()
        time.sleep(2)
    # 备注
    def send_xjjh_beizhu(self,connect):
        self.get_xjjh_beizhu().send_keys(connect)
    # 勾选-添加巡检点
    def send_xjjh_gouxuanjjdd(self):
        self.get_xjjh_gouxuanjjdd().click()
        time.sleep(2)
    # 【添加】
    def send_xjjh_tianjiaanniu(self):
        self.get_xjjh_tianjiaanniu().click()
        time.sleep(1)
    # 【取消】
    # def send_xjjh_quxiaoanniu(self):
    #     self.get_xjjh_quxiaoanniu().click()
    #     time.sleep(2)


    # 添加成功后【添加成功】断言
    def get_xjjh_xjtjdy(self):
        return self.get_xjjh_tjdy().text


# 修改巡检计划操作层
 # 添加-巡检编号
    def send_xjjh_xjxjbh(self,xjxjbh):
        self.get_xjjh_xjxjbh().clear()
        self.get_xjjh_xjxjbh().send_keys(xjxjbh)
    # 添加-计划名称
    def send_xjjh_xjjhmc(self,xjjhmc):
        self.get_xjjh_xjjhmc().clear()
        self.get_xjjh_xjjhmc().send_keys(xjjhmc)
    # 添加-巡检类型
    def send_xjjh_xjxjlx(self):
        self.get_xjjh_xjxjlx().click()
        time.sleep(1)
    # 添加-巡检类型-下拉框
    def send_xjjh_xjxjlxxlk(self):
        self.get_xjjh_xjxjlx().click()
        time.sleep(1)
    # 巡检周期
    def send_xjjh_xjxjzq(self):
        self.get_xjjh_xjxjzq().click()
        time.sleep(2)
    # 巡检周期-下拉框
    def send_xjjh_xjxjzqxlk(self):
        self.get_xjjh_xjxjzqxlk().click()
        time.sleep(2)
    # 开始日期
    def send_xjjh_xjkaishiriqi(self):
        self.get_xjjh_xjkaishiriqi().click()
        time.sleep(2)
    # 开始日期-下拉框
    def send_xjjh_xjksrqxlk(self):
        self.get_xjjh_xjksrqxlk().click()
        time.sleep(2)
    # 结束日期
    def send_xjjh_xjjieshuriqi(self):
        self.get_xjjh_xjjieshuriqi().click()
        time.sleep(2)
    # 结束日期-下拉框
    def send_xjjh_xjjsrqxlk(self):
        self.get_xjjh_xjjsrqxlk().click()
        time.sleep(2)
    # 备注
    def send_xjjh_xjbeizhu(self,xjconnect):
        self.get_xjjh_xjbeizhu().clear()
        self.get_xjjh_xjbeizhu().send_keys(xjconnect)
    # 勾选-修改巡检点
    def send_xjjh_xjgouxuanjjdd(self):
        self.get_xjjh_xjgouxuanjjdd().click()
        time.sleep(2)
    # 【修改】
    def send_xjjh_xjtianjiaanniu(self):
        self.get_xjjh_xjtianjiaanniu().click()
        time.sleep(2)

        # 修改成功后【修改成功】断言
    def get_xjjh_xjxgcg(self):
        return self.get_xjjh_xgcg().text

    # # 【取消】
    # def send_xjjh_xjquxiaoanniu(self):
    #     self.get_xjjh_xjquxiaoanniu().click()
    #     time.sleep(2)



# 查看-确定
    def send_xjjh_ckqd(self):
        self.get_xjjh_ckqd().click()
        time.sleep(2)

#  业务层
class xjjhyewu(xjjhcaocuo):
    def __init__(self):
        xjjhcaocuo.__init__(self)

    def add_xjjh_notice(self,xjbh,jhmc,connect,xjxjbh,xjjhmc,xjconnect):
        # 添加
        self.send_xjjh_tianjia()
        self.send_xjjh_xjbh(xjbh)
        self.send_xjjh_jhmc(jhmc)
        # 1
        self.send_xjjh_xjlx()
        self.send_xjjh_xjlxxlk()
        self.send_xjjh_xjzq()
        self.send_xjjh_xjzqxlk()
        self.send_xjjh_kaishiriqi()
        self.send_xjjh_ksrqxlk()
        self.send_xjjh_jieshuriqi()
        self.send_xjjh_jsrqxlk()
        self.send_xjjh_beizhu(connect)
        self.send_xjjh_gouxuanjjdd()
        self.send_xjjh_tianjiaanniu()
        # self.send_xjjh_quxiaoanniu()

        # aaa = self.get_xjjh_xjtjdy()
        # bbb = self.get_xjjh_xjxgcg()

        # 修改
        self.send_xjjh_xiugai()
        self.send_xjjh_xjxjbh(xjxjbh)
        self.send_xjjh_xjjhmc(xjjhmc)
        self.send_xjjh_xjxjlx()
        self.send_xjjh_xjxjlxxlk()
        self.send_xjjh_xjkaishiriqi()
        self.send_xjjh_xjksrqxlk()
        self.send_xjjh_xjjieshuriqi()
        self.send_xjjh_xjjsrqxlk()
        self.send_xjjh_xjbeizhu(xjconnect)
        self.send_xjjh_xjgouxuanjjdd()
        self.send_xjjh_xjtianjiaanniu()
        # self.send_xjjh_xjquxiaoanniu()


        # 查看
        self.send_xjjh_chakan()
        self.send_xjjh_ckqd()

        # 删除
        self.send_xjjh_shanchu()
        self.send_xjjh_xjshanchu()

        ccc = self.get_xjjh_xjscsb()

        # print(aaa,bbb,ccc)

        return ccc

if __name__ == '__main__':
    xjjhyewu().add_xjjh_notice(111,2111,3,44444,555555,6)

