import unittest
from recursives.r3.summation import summation

class MyTestCase(unittest.TestCase):


    def test_something(self):
        self.assertEqual(summation(2), 3)

    def test_something_1(self):
        self.assertEqual(summation(3), 6)

    def test_something_2(self):
        self.assertEqual(summation(4), 10)


if __name__ == '__main__':
    unittest.main()
