import unittest
from extras.e6 import e6


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(e6.is_parallel((3, -1), (-9, 3)), True)

    def test_something_2(self):
        self.assertEqual(e6.is_parallel_without_equal((3, -1), (-9, 3)), True)

    def test_something_3(self):
        self.assertEqual(e6.is_parallel_without_equal((3, -1), (-7, 3)), False)

    def test_something_4(self):
        self.assertEqual(e6.is_parallel((3, -1), (-7, 3)), False)


if __name__ == '__main__':
    unittest.main()
