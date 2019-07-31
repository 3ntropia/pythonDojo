import unittest
from extras.e3 import e3


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(e3.split_email("alguien@uade.edu.ar"), ("alguien", "uade", "edu", "ar"))


if __name__ == '__main__':
    unittest.main()
