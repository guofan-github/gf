import time
import unittest

from pages.wshgdpage import wshgdyewu


class test_wshgd(unittest.TestCase):

    def test_shenhe(self):
        r = wshgdyewu().shenhe_wshgd()
        print(r)
        self.assertEqual(r, '审核成功')

