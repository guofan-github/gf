import unittest

from pages.jcsspage import jcssyewu


class testsheshi(unittest.TestCase):

    # 测试用例
    def test_sheshi(self):
        r = jcssyewu().jcss_sheshi()
        self.assertEqual(r, '添加成功')

    def test_shenqing(self):
        r = jcssyewu().jcss_shenqing()
        self.assertEqual(r, '申请成功,等待批复')