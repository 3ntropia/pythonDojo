import unittest
from functions.function1 import biggerNumber


class TestBiggerNumber(unittest.TestCase):

    def test_biggerA(self):
        self.assertEqual('3', biggerNumber.bigger(3, 2, 1))

    def test_biggerB(self):
        self.assertEqual('3', biggerNumber.bigger(2, 3, 1))

    def test_biggerC(self):
        self.assertEqual('3', biggerNumber.bigger(1, 2, 3))

    def test_bigger_a_equal_b(self):
        self.assertEqual('No hay mayores', biggerNumber.bigger(3, 3, 1))

    def test_bigger_a_equal_c(self):
        self.assertEqual('No hay mayores', biggerNumber.bigger(5, 4, 5))

    def test_no_bigger(self):
        self.assertEqual('No hay mayores', biggerNumber.bigger(3, 3, 3))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestBiggerNumber('test1'))
    unittest.TextTestRunner().run(suite)
