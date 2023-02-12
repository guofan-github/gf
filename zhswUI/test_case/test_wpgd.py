import unittest
from pages.wpgdpage import wpgdyewu

class wpgdcase(unittest.TestCase):

    def test_wpgd(self):
        xxx = wpgdyewu().add_wpgd_notice()
        print(xxx)

        self.assertEqual(xxx, "添加成功")

if __name__ == '__main__':
    wpgdcase().test_wpgd()
