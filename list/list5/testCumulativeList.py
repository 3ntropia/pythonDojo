import unittest
from list.list5 import cumulativeList


class MyTestCase(unittest.TestCase):

    def test_cumulative_list(self):
        self.assertEqual(cumulativeList.sum_array_cumulative([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_cumulative_list_not_sorted(self):
        self.assertEqual(cumulativeList.sum_array_cumulative([6, 5, 3, 4]), [6, 11, 14, 18])


if __name__ == '__main__':
    unittest.main()
