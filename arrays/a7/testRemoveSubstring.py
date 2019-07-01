import unittest
from arrays.a7 import removeString

class MyTestCase(unittest.TestCase):

    __string__ = "abcdefghijklmnopqrstuvwxyz"

    def test_substring_slicing(self):
        self.assertEqual(removeString.remove_substring(MyTestCase.__string__, 10, 5), "abcdefghijpqrstuvwxyz")

    def test_substring(self):
        self.assertEqual(removeString.remove_substring_not_slicing(MyTestCase.__string__, 10, 5), "abcdefghijpqrstuvwxyz")
