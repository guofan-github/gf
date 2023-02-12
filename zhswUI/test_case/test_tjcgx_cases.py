import unittest
from pages.tjcgxpage import TjcgxYewu


class tjcgxcase(unittest.TestCase):

    def test_tjcgx(self):
        r = TjcgxYewu().tjcgx_yewu('45', '赵四', 'asd')
        self.assertEqual(r, '成功')