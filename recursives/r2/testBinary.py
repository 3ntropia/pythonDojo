import unittest
from recursives.r2.binary import binarty_to_decimal


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(binarty_to_decimal("01"), 1)

    def test_something_2(self):
        self.assertEqual(binarty_to_decimal("100"), 4)

    def test_something_3(self):
        self.assertEqual(binarty_to_decimal("101"), 5)

    def test_something_4(self):
        self.assertEqual(binarty_to_decimal("11"), 3)

    def test_something_5(self):
        self.assertEqual(binarty_to_decimal("1000"), 8)


if __name__ == '__main__':
    unittest.main()
