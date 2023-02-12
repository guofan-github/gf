import unittest
from pages.ypgdpage import ypgdyewu

class ypgdcase(unittest.TestCase):

    def test_ypgd(self):
        eee = ypgdyewu().add_ypgd_notice()
        print(eee)



if __name__ == '__main__':
    ypgdcase().test_ypgd()