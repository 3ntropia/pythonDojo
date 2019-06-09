import unittest
from list.list6 import removeRepeated


class MyTestCase(unittest.TestCase):

    __array__ = ['a', 'b', 'c', 'd', 'e']
    __words_to_remove__ = ['f', 'e', 'g', 'b']
    __no_words_to_remove__ = ['f', 'g', 'g', 'h']

    def test_remove_some(self):
        self.assertEqual(removeRepeated.remove_repeated(MyTestCase.__array__, MyTestCase.__words_to_remove__), ['a', 'c', 'd'])

    def test_no_remove_some(self):
        self.assertEqual(removeRepeated.remove_repeated(MyTestCase.__array__, MyTestCase.__no_words_to_remove__), MyTestCase.__array__)


if __name__ == '__main__':
    unittest.main()
