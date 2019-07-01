import unittest
from arrays.a9 import a9

class MyTestCase(unittest.TestCase):

    __string = "oireutowkcscfzmxcuhqoiquwelasmcanm"

    def test_something(self):
        self.assertEqual(a9.last_values(MyTestCase.__string, 7), "asmcanm")
