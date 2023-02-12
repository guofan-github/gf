import unittest
from pages.bzsjpage import bzsjyewu

class bzsjcase(unittest.TestCase):


    def test_bzsj(self):
        ddd = bzsjyewu().add_bzsj_notice()
        print(ddd)
        self.assertEqual(ddd,"成功")

if __name__ == '__main__':
    bzsjcase().test_bzsj()