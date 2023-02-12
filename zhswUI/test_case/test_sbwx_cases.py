import unittest

from pages.sbwxpage import sbwxyewu


class testsbwx(unittest.TestCase):

    def test_sbwx(self):
        r = sbwxyewu().wcjx_sbwx()
        self.assertEqual(r, '修改成功')

