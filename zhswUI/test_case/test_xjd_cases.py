import unittest
from pages.xjddpage import xjddyewu


class xjddcase(unittest.TestCase):

    # 测试用例
    def test_xjdd(self):
        r = xjddyewu().xjdd_yewu("P001", "1", "1", "1", "P111", "P111", "P111", "P111")
        print(r)
        self.assertEqual(r, "删除成功")


if __name__ == '__main__':
    xjddcase().test_xjdd()