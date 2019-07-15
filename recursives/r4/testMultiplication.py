import unittest
from recursives.r4.multiplication import multiplication


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(multiplication(4, 5), 20)

    def test_something_reverse(self):
        self.assertEqual(multiplication(5, 4), 20)

    def test_something_1(self):
        self.assertEqual(multiplication(6, 6), 36)


if __name__ == '__main__':
    unittest.main()
