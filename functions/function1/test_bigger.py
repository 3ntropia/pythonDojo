import unittest
from functions import function1


class TestFunctions(unittest.TestCase):

    def test_biggerA(self):
        self.assertEqual('3', function1.bigger(int(3), int(2), int(1)))

    def test_biggerB(self):
        self.assertEqual('3', function1.bigger(int(2), int(3), int(1)))

    def test_biggerC(self):
        self.assertEqual('3', function1.bigger(int(1), int(2), int(3)))

    def test_no_bigger(self):
        self.assertEqual('No hay mayores', function1.bigger(int(3), int(3), int(3)))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestFunctions('test1'))
    unittest.TextTestRunner().run(suite)
