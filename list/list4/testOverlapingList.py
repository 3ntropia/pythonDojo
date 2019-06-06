import unittest
from list.list4 import overlapingList


class MyTestCase(unittest.TestCase):

    __array__ = [1, 2, 3, 4, 3]
    __array2__ = [5, 6, 7, 8, 6, 9, 10]
    __overlap_array__ = [16, 19, 3, 6, 2, 9, 9, 4]

    def test_is_overlap(self):
        self.assertEqual(overlapingList.is_overlap(MyTestCase.__array__, MyTestCase.__overlap_array__), True)

    def test_is_not_overlap(self):
        self.assertEqual(overlapingList.is_overlap(MyTestCase.__array__, MyTestCase.__array2__), False)

    def test_is_overlap_naive(self):
        self.assertEqual(overlapingList.is_overlap_naive(MyTestCase.__array__, MyTestCase.__overlap_array__), True)

    def test_is_not_overlap_naive(self):
        self.assertEqual(overlapingList.is_overlap_naive(MyTestCase.__array__, MyTestCase.__array2__), False)


if __name__ == '__main__':
    unittest.main()
