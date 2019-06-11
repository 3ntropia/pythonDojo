import unittest
from list.list9 import normalize


class MyTestCase(unittest.TestCase):

    def test_normalize(self):
        self.assertEqual(normalize.normalize([1, 1, 2]), [0.25, 0.25, 0.50])


if __name__ == '__main__':
    unittest.main()
