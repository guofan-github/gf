import unittest
from unittest import skip

import ddt

from common.read_data import Read
from page.geomagnetism_management import GeomagnetismManagementBusiness, DelTestData
from webdriver.GetDriver import GetDriver



@ddt.ddt
class TestGeomagnetismManagement(unittest.TestCase):

    # 使用夹具：每次用例执行完新增一条数据，就会清理掉一条数据
    def tearDown(self) -> None:
        DelTestData().del_data()
        GetDriver().browser_close()

    # 通过unittest测试地磁管理新增
    # 从excel中获取测试数据
    data = Read().get_data('新增地磁', 'Sheet1')

    # 使用ddt数据驱动
    # @skip('跳过这条用例')
    @ddt.data(*data)
    # @ddt.data(['ddd','ccc'])
    @ddt.unpack
    def test_geomagnetism_add(self, name, id):
        r = GeomagnetismManagementBusiness().add_geomagnetism(name, id)
        self.assertEqual(r, '添加成功！')
