import unittest
from arrays.a10 import a10


class MyTestCase(unittest.TestCase):

    __string = "lkfdsajld12831sdfj128043023cxxsqz"

    def test_something(self):
        self.assertEqual(a10.count_char_numbers(MyTestCase.__string), (14, 19))


if __name__ == '__main__':
    unittest.main()
