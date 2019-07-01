import unittest
from arrays.a8 import a8

class MyTestCase(unittest.TestCase):

    __string = "z x d e y b"

    def test_something(self):
        self.assertEqual(a8.sort_string(MyTestCase.__string), "b d e x y z")

