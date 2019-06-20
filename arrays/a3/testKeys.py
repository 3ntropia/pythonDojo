import unittest
from arrays.a3.keys import get_keys


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(get_keys("18293"), ("123", "89"))


if __name__ == '__main__':
    unittest.main()
