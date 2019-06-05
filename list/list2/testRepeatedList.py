import unittest
from list.list2 import repeatedList


class MyTestCase(unittest.TestCase):
    __repeated_array__ = [1, 2, 3, 4, 5, 3]
    __repeated_array2__ = [1, 2, 3, 4, 5, 5, 5, 3]
    __not_repeated_array__ = [8, 9, 3, 4, 5, 6, 7, 2]

    def test_creation_list(self):
        self.assertEqual(len(repeatedList.create_list()), 50)

    def test_has_repeated_elements(self):
        self.assertEqual(repeatedList.has_repeated_element(MyTestCase.__repeated_array__), True)

    def test_has_not_repeated_elements(self):
        self.assertEqual(repeatedList.has_repeated_element(MyTestCase.__not_repeated_array__), False)

    def test_repeated_with_set(self):
        self.assertEqual(repeatedList.has_repeated_element_set(MyTestCase.__repeated_array__), True)

    def test_not_repeated_with_set(self):
        self.assertEqual(repeatedList.has_repeated_element_set(MyTestCase.__not_repeated_array__), False)

    def test_repeated_naive(self):
        self.assertEqual(repeatedList.has_repeated_element_naive(MyTestCase.__repeated_array__), True)

    def test_not_repeated_naive(self):
        self.assertEqual(repeatedList.has_repeated_element_naive(MyTestCase.__not_repeated_array__), False)

    def test_unique_set(self):
        self.assertEqual(repeatedList.unique_list_set(MyTestCase.__repeated_array2__), [1, 2, 3, 4, 5])

    def test_unique_naive(self):
        self.assertEqual(repeatedList.unique_list_naive(MyTestCase.__repeated_array2__), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
