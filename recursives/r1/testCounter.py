import unittest
from recursives.r1 import r1

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(r1.digit_counter(0, 0, 333), 3)

    def test_something_2(self):
        self.assertEqual(r1.digit_counter(0, 0, 56), 2)


if __name__ == '__main__':
    unittest.main()
