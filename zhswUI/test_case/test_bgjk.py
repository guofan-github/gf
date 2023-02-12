import unittest
from pages.bgjkpage import bgjkyewu

class bgjkcase(unittest.TestCase):

    def test_bgjk(self):
        eee = bgjkyewu().add_bgjk_notice()
        print(eee)


if __name__ == '__main__':
    bgjkcase().test_bgjk()

