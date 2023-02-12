import time
import unittest
from pages.shlbpage import ShlbYewu


class ShlbCase(unittest.TestCase):

    def test_shld(self):
        time.sleep(5)
        r = ShlbYewu().shlb_yewu()
        self.assertEqual(r, '成功')