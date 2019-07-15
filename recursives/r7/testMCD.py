import unittest
from recursives.r7.MCD import mcd, mcd_non_loop


class MyTestCase(unittest.TestCase):

    # MCD(X, X) = X
    def test_first_property(self):
        self.assertEqual(mcd(4, 4), 4)

    def test_first_property_loop(self):
        self.assertEqual(mcd_non_loop(4, 4), 4)

    def test_first_property_2(self):
        self.assertEqual(mcd(11, 11), 11)

    # MCD(X, Y) = MCD(Y, X)
    def test_second_property(self):
        self.assertEqual(mcd(4, 5), mcd(5, 4))

    def test_second_property_loop(self):
        self.assertEqual(mcd_non_loop(4, 5), mcd_non_loop(5, 4))

    # Si X > Y = > MCD(X, Y) = MCD(X–Y, Y).
    def test_third_property(self):
        self.assertEqual(mcd(15, 5), mcd(10, 5))

    def test_third_property_loop(self):
        self.assertEqual(mcd_non_loop(15, 5), mcd_non_loop(10, 5))


if __name__ == '__main__':
    unittest.main()

