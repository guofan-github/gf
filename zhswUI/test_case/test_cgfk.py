import unittest
from pages.cgfkpage import cgfkyewu

class cgfkcase(unittest.TestCase):
    def test_cgfk(self):
        bbb = cgfkyewu().add_cgfk_notice()
        print(bbb)

if __name__ == '__main__':
    cgfkcase().test_cgfk()