import unittest

from pages.dtdwpage import dtdwyewu


class test_dtdw(unittest.TestCase):

    def test_ditu(self):
        r = dtdwyewu().dtdw_ditu()
        self.assertEqual(r, '武汉泵站')
        