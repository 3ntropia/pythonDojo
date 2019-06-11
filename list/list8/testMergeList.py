import unittest
from list.list8 import mergeList


class MyTestCase(unittest.TestCase):

    __array__ = mergeList.build_list(30)
    __array2__ = mergeList.build_list(30)
    __array3__ = [34, 12, 2, 19, 18, 25, 42, 3, 25, 32, 39, 26, 2, 48, 30, 12, 3, 43, 18, 16, 47, 6, 39, 31, 37, 49,
                  24, 3, 11, 5]
    __array4__ = [1, 14, 2, 16, 25, 29, 46, 12, 50, 43, 32, 10, 30, 27, 7, 17, 22, 46, 32, 21, 45, 28, 27, 23, 22,
                  21, 37, 27, 32, 15]

    def test_something(self):
        print(MyTestCase.__array__)
        print(MyTestCase.__array2__)
        self.assertEqual(mergeList.merge_list_naive(MyTestCase.__array3__, MyTestCase.__array4__),
                         [12, 2, 25, 25, 32, 32, 32, 2, 30, 12, 43, 16, 37])

    def test_something_2(self):
        print(MyTestCase.__array__)
        print(MyTestCase.__array2__)
        self.assertEqual(mergeList.merge_list_naive(MyTestCase.__array3__, MyTestCase.__array4__),
                         mergeList.merge_list_new(MyTestCase.__array3__, MyTestCase.__array4__))


if __name__ == '__main__':
    unittest.main()
