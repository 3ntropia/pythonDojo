import unittest
from functions.function5 import returnMoney


class MyTestCase(unittest.TestCase):
    def test_no_given_back(self):
        self.assertEqual(returnMoney.return_money(10, 10), "No hay vuelto")

    def test_no_given_back_error(self):
        self.assertEqual(returnMoney.return_money(30, 20), "Dinero recibido insuficiente")

    def test_return_1(self):
        self.assertEqual(returnMoney.return_money(10, 20), "$10 x1.0 ")

    def test_return_2(self):
        self.assertEqual(returnMoney.return_money(10, 520), "$500 x1.02 ")


if __name__ == '__main__':
    unittest.main()
