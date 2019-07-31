import unittest
from extras.e5 import e5


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(e5.is_orthogonal((2, 3), (-3, 2)), True)

    def test_something_2(self):
        self.assertEqual(e5.is_orthogonal((2, 3), (-5, 6)), False)


if __name__ == '__main__':
    unittest.main()
