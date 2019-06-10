import unittest
from list.list7 import sortList


class MyTestCase(unittest.TestCase):
    def test_not_sorted(self):
        self.assertEqual(sortList.is_sorted([2, 9, 3, 8]), False)

    def test_not_sorted_letters(self):
        self.assertEqual(sortList.is_sorted(['d', 'a', 'h']), False)

    def test_is_sorted(self):
        self.assertEqual(sortList.is_sorted([4, 5, 6]), True)

    def test_is_sorted_letters(self):
        self.assertEqual(sortList.is_sorted(['g', 'h', 'i']), True)


if __name__ == '__main__':
    unittest.main()
