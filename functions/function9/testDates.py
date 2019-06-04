import unittest
from functions.function9 import operateDate


class MyTestCase(unittest.TestCase):
    def test_add_one_date(self):
        self.assertEqual(operateDate.next_date(22, 1, 2019), (23, 1, 2019))

    def test_add_date_last_day(self):
        self.assertEqual(operateDate.next_date(30, 1, 2019), (31, 1, 2019))

    def test_add_date_change_month(self):
        self.assertEqual(operateDate.next_date(31, 1, 2019), (1, 2, 2019))

    def test_add_date_thirty_month(self):
        self.assertEqual(operateDate.next_date(30, 4, 2019), (1, 5, 2019))

    def test_add_date_invalid(self):
        self.assertEqual(operateDate.next_date(30, 30, 2019), (30, 30, 2019))

    def test_add_date_february(self):
        self.assertEqual(operateDate.next_date(28, 2, 2019), (1, 3, 2019))

    def test_add_n_days(self):
        self.assertEqual(operateDate.add_n_days(22, 1, 2019, 3), (25, 1, 2019))

    def test_diff_dates(self):
        self.assertEqual(operateDate.diff_dates(10, 1, 2019, 15, 1, 2019), 5)

    def test_diff_dates_change_month(self):
        self.assertEqual(operateDate.diff_dates(20, 1, 2019, 1, 2, 2019), 12)


if __name__ == '__main__':
    unittest.main()
