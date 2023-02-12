import unittest

from pages.bzxxpage import bzxxyewu


class testbzxx(unittest.TestCase):

    # 添加
    def test_tianjia(self):
        r = bzxxyewu().bzxx_tianjia()
        self.assertEqual(r, '成功')

    # 修改
    def test_xiugai(self):
        r = bzxxyewu().bzxx_xiugai()
        self.assertEqual(r, '成功')

    def test_shanchu(self):
        r = bzxxyewu().bzxx_shanchu()
        self.assertEqual(r, '成功')

