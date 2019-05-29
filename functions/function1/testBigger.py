import unittest
from functions.function1 import biggerNumber


class TestBiggerNumber(unittest.TestCase):

    def test_biggerA(self):
        self.assertEqual('3', biggerNumber.bigger(int(3), int(2), int(1)))

    def test_biggerB(self):
        self.assertEqual('3', biggerNumber.bigger(int(2), int(3), int(1)))

    def test_biggerC(self):
        self.assertEqual('3', biggerNumber.bigger(int(1), int(2), int(3)))

    def test_no_bigger(self):
        self.assertEqual('No hay mayores', biggerNumber.bigger(int(3), int(3), int(3)))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestBiggerNumber('test1'))
    unittest.TextTestRunner().run(suite)
