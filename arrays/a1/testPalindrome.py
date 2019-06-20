import unittest
from arrays.a1.palindrome import is_palindrome


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_palindrome("abcba"), True)


if __name__ == '__main__':
    unittest.main()
