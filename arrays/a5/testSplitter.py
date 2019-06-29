import unittest
from arrays.a5 import splitter

class MyTestCase(unittest.TestCase):

    __string__ = "aaa a bb c dddd ddd gg y eeeee ffff ooo uu pp qqqqqq"

    def test_split_five(self):
        self.assertEqual(splitter.filter_word_len_v1(MyTestCase.__string__, 5), "eeeee qqqqqq")

    def test_split_six(self):
        self.assertEqual(splitter.filter_word_len_v1(MyTestCase.__string__, 6), "qqqqqq")

    def test_split_list_six(self):
        self.assertEqual(splitter.filter_word_len_v2(MyTestCase.__string__, 6), ["qqqqqq"])

    def test_split_filter_six(self):
        self.assertEqual(splitter.filter_word_len_v3(MyTestCase.__string__, 6), ["qqqqqq"])



if __name__ == '__main__':
    unittest.main()
