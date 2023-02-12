import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.businesspage import businesspage
from util.config import host_port


# 元素定位
class bzsjpage(businesspage):
    def __init__(self):
        businesspage.__init__(self)
        self.driver.get(f'http://{host_port}/water/#/gms/pumpdata')
        time.sleep(2)

    # 【删除】按钮
    def get_bzsj_shanchu(self):
        return self.driver.find_element_by_xpath('/html/body/div/section/section/main/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[12]/div/button/span')

    # 断言【成功】文本
    def get_bzsj_chenggong(self):
        return self.driver.find_element_by_xpath('/html/body/div[2]/p')



    # 断言【成功】文本
    # def get_bzsj_chenggong(self):
    #     serarch_obj = WebDriverWait(self.driver, 5, 0.6).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/p')))
    #     return serarch_obj.text
    # # 冻结
    # def get_bzsj_dongjie(self):
    #     self.driver.execute_script('setTimeout(function(){debugger},5000)')


# 操作层
class bzsjcaozuo(bzsjpage):
    def __init__(self):
        bzsjpage.__init__(self)

    # 【删除】按钮
    def click_bzsj_shanchu(self):
        self.get_bzsj_shanchu().click()


    # 断言【成功】文本
    def get_bzsj_bzchenggong(self):
        return self.get_bzsj_chenggong().text



# 业务层
class bzsjyewu(bzsjcaozuo):
    def __init__(self):
        bzsjcaozuo.__init__(self)

    def add_bzsj_notice(self):
        self.click_bzsj_shanchu()
        # self.get_bzsj_dongjie()
        time.sleep(1)
        aaa = self.get_bzsj_bzchenggong()

        print(aaa)
        return aaa

if __name__ == '__main__':
    bzsjyewu().add_bzsj_notice()