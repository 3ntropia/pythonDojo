import unittest
from arrays.a9 import lastValues

class MyTestCase(unittest.TestCase):

    __string = "oireutowkcscfzmxcuhqoiquwelasmcanm"

    def test_something(self):
        self.assertEqual(lastValues.last_values(MyTestCase.__string, 7), "asmcanm")
