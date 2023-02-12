import time
import unittest
from pages.xjjhpage import xjjhyewu


class xjjhcase(unittest.TestCase):


    def test_xjjh(self):
        csyl = xjjhyewu().add_xjjh_notice('101','102','1050023','222','333','987456')
        print(csyl)
        self.assertEqual(csyl, "删除失败")


if __name__ == '__main__':
    xjjhcase().test_xjjh()
