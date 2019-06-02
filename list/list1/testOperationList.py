import unittest
from list.list1 import l1


class MyTestCase(unittest.TestCase):

    def test_sum_list(self):
        self.assertEqual(l1.sum_list([1, 2, 3, 4]), 10)


if __name__ == '__main__':
    unittest.main()
