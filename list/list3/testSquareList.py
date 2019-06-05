import unittest
from list.list3 import squareList


class MyTestCase(unittest.TestCase):

    def test_create_square_list(self):
        self.assertEqual(squareList.first_squares_list(5), [1, 4, 9, 16, 25])


