import unittest
from list.list1 import operationsList


class MyTestCase(unittest.TestCase):

    def test_sum_list(self):
        self.assertEqual(operationsList.sum_list([1, 2, 3, 4]), 10)

    def test_remove_from_list(self):
        self.assertEqual(operationsList.remove_from_list([1, 2, 3, 4], 2), [1, 3, 4])

    def test_remove_from_list_repeated(self):
        self.assertEqual(operationsList.remove_from_list([1, 2, 2, 3, 4], 2), [1, 3, 4])

    def test_remove_old_school(self):
        self.assertEqual(operationsList.remove_from_list_old_school([1, 2, 3, 4], 2), [1, 3, 4])

    def test_both_method_equals(self):
        old_style = operationsList.remove_from_list_old_school([1, 2, 3, 4], 2)
        easy_style = operationsList.remove_from_list([1, 2, 3, 4], 2)
        self.assertEqual(old_style, easy_style)

    def test_palindrome(self):
        self.assertEqual(operationsList.is_palindrome([1, 2, 3, 2, 1]), True)

    def test_not_palindrome(self):
        self.assertEqual(operationsList.is_palindrome([1, 4, 3, 2, 1]), False)


if __name__ == '__main__':
    unittest.main()
