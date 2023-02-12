import unittest

from pages.sblbpage import sblbyewu


class testsblb(unittest.TestCase):
    # 分配设备测试
    def test_fenpei(self):
        r = sblbyewu().sblb_fpsb()
        self.assertEqual(r, '分配成功')

    # 待批列表测试
    def test_dplb(self):
        r = sblbyewu().sblb_dplb()
        self.assertEqual(r, '已批复')

    # 修改
    def test_xiugai(self):
        r = sblbyewu().sblb_xiugai()
        self.assertEqual(r, '修改成功')


