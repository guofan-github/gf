import os
import time


class Ci:

    def checkout(self):
        print('************ checkout **************')
        if os.path.exists('./woniusales'):
            os.system('rd /s/q woniusales')
            time.sleep(1)
        os.system('svn co svn://jacky-pc/woniusales/ --username jacky --password 123456')
        time.sleep(3)

    def build(self):
        print('************ build **************')
        os.system('ant -f D:/WoniuSalesSVN/build.xml')
        time.sleep(3)

    def deploy(self):
        print('************ deploy **************')
        os.system('echo y | pscp -pw 123456 D:/WoniuSalesSVN/woniusales.war '
                  'root@172.16.6.138:/opt/tomcat9/webapps/')
        time.sleep(20)

    def test(self):
        from CBT.ATM.module.module_login import ModuleLogin

        TEST_VERSION = '0.05'

        login = ModuleLogin(TEST_VERSION)
        login.main_test()

    def start(self):
        self.checkout()
        self.build()
        self.deploy()
        self.test()


if __name__ == '__main__':
    Ci().start()