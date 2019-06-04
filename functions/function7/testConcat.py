import unittest
from functions.function7 import concat


class MyTestCase(unittest.TestCase):

    def test_concat(self):
        self.assertEqual(concat.concat(1, 2), "12")

    def test_concat_2(self):
        self.assertEqual(concat.concat(123, 22222), "12322222")

    def test_concat_3(self):
        self.assertEqual(concat.concat(1, 41232), "141232")

    def test_concat_4(self):
        self.assertEqual(concat.concat(43, 32), "4332")


if __name__ == '__main__':
    unittest.main()
