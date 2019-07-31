import unittest
from extras.e2 import e2


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(e2.split_tuple((1, 2, 2010)), "1 Febrero 2010")


if __name__ == '__main__':
    unittest.main()
