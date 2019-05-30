import unittest
from functions.function4 import spendCalculator


class MyTestCase(unittest.TestCase):

    def test_one_trip(self):
        self.assertEqual(spendCalculator.spend_calculator(1), 20)

    def test_negative_trip(self):
        self.assertEqual(spendCalculator.spend_calculator(-1), 0)

    def test_zero_trip(self):
        self.assertEqual(spendCalculator.spend_calculator(0), 0)

    def test_minus_twenty_trip(self):
        self.assertEqual(spendCalculator.spend_calculator(20), 400)

    def test_first_step_trip(self):
        self.assertEqual(spendCalculator.spend_calculator(25), 500)

    def test_second_step_trip(self):
        self.assertEqual(spendCalculator.spend_calculator(35), 700)

    def test_third_step_trip(self):
        self.assertEqual(spendCalculator.spend_calculator(45), 1700)


if __name__ == '__main__':
    unittest.main()
