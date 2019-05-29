import unittest
from functions.function3 import sumSquares


class TestSumSquares(unittest.TestCase):
    def test_sum_zero(self):
        self.assertEqual(sumSquares.sum_minor_n(0), 0)

    def test_sum_minor_number(self):
        self.assertEqual(sumSquares.sum_minor_n(24), 1)

    def test_sum_minor_number(self):
        self.assertEqual(sumSquares.sum_minor_n(106), 26)

    def test_sum_minor_number(self):
        self.assertEqual(sumSquares.sum_minor_n(24), 1)

    def test_sum_equal(self):
        self.assertEqual(sumSquares.sum_minor_n(26), 26)

    def test_sum_equal(self):
        self.assertEqual(sumSquares.sum_minor_n(107), 107)

    def test_sum_equal(self):
        self.assertEqual(sumSquares.sum_minor_n(108), 107)

if __name__ == '__main__':
    unittest.main()
