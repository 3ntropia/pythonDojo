import unittest
from arrays.a4.roman import roman_converter


class MyTestCase(unittest.TestCase):

    def test_roman_thounsands(self):
        self.assertEqual(roman_converter(2019), 'MMXIX')

    def test_roman_hundreds(self):
        self.assertEqual(roman_converter(179), 'CLXXIX')

    def test_roman_tens(self):
        self.assertEqual(roman_converter(14), 'XIV')


if __name__ == '__main__':
    unittest.main()
