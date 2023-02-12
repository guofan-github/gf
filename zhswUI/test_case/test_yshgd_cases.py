import unittest
from pages.yshgdpage import yshgdyewu

class yshgdcase(unittest.TestCase):

    def test_ysh(self):
        r = yshgdyewu().yshgd_yewu()
        self.assertEqual(r, '删除成功')


if __name__ == '__main__':
    yshgdcase().test_ysh()