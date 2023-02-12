import unittest
from pages.jsglpage import jsglyewu

class jsglcase(unittest.TestCase):

    def test_jsgl(self):
        eee = jsglyewu().add_xjjh_notice()
        print(eee)

        self.assertEqual(eee, "授权成功")

if __name__ == '__main__':
    jsglcase().test_jsgl()

