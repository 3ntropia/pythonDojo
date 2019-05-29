import unittest
from functions.function2 import validDate


class TestValidDate(unittest.TestCase):

    def test_invalid_date(self):
        self.assertEqual(validDate.is_date_valid(3, 4, 5), False)

    def test_invalid_day_2(self):
        self.assertEqual(validDate.is_date_valid(32, 10, 2019), False)

    def test_invalid_day_3(self):
        self.assertEqual(validDate.is_date_valid(32, 10, 2019), False)

    def test_invalid_day_4(self):
        self.assertEqual(validDate.is_date_valid(-5, 10, 2019), False)

    def test_invalid_day_5(self):
        self.assertEqual(validDate.is_date_valid(0, 10, 2019), False)

    def test_invalid_month(self):
        self.assertEqual(validDate.is_date_valid(10, 13, 2019), False)

    def test_invalid_month_2(self):
        self.assertEqual(validDate.is_date_valid(10, -13, 2019), False)

    def test_invalid_year(self):
        self.assertEqual(validDate.is_date_valid(10, 11, 1899), False)

    def test_valid_leap_year(self):
        self.assertEqual(validDate.is_leap_year(2020), True)

    def test_invalid_leap_year(self):
        self.assertEqual(validDate.is_leap_year(2018), False)

    def test_valid_date(self):
        self.assertEqual(validDate.is_date_valid(29, 5, 2019), True)

    def test_valid_date_february(self):
        self.assertEqual(validDate.is_date_valid(28, 2, 2019), True)

    def test_invalid_date_february(self):
        self.assertEqual(validDate.is_date_valid(29, 2, 2019), False)


if __name__ == '__main__':
    unittest.main()
