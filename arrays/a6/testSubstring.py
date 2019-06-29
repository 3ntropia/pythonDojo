import unittest
from arrays.a6 import substring


class MyTestCase(unittest.TestCase):

    __string__ = "abcdefghijklmnopqrstuvwxyz"

    def test_substring_slicing(self):
        self.assertEqual(substring.substring_slicing(MyTestCase.__string__, 10, 5), "klmno")

    def test_substring(self):
        self.assertEqual(substring.substring_not_slicing(MyTestCase.__string__, 10, 5), "klmno")
