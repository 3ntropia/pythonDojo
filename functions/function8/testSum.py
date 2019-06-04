import unittest
from functions.function8 import strangeSum


class MyTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(strangeSum.strange_sum(3), 3702)

    def test_sum_2(self):
        self.assertEqual(strangeSum.strange_sum(2), 2468)

    def test_sum_3(self):
        self.assertEqual(strangeSum.strange_sum(6), 7404)

    def test_sum_error(self):
        self.assertEqual(strangeSum.strange_sum(0), -1)

    def test_sum_error_2(self):
        self.assertEqual(strangeSum.strange_sum(10), -1)


if __name__ == '__main__':
    unittest.main()
