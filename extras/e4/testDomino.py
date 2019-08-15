import unittest
from extras.e4 import e4


class MyTestCase(unittest.TestCase):

    domino_1_1 = (1, 1)
    domino_1_2 = (1, 2)
    domino_3_4 = (3, 4)
    domino_4_4 = (4, 4)
    domino_2_5 = (2, 5)

    def test_something(self):
        self.assertEqual(e4.can_be_fit(MyTestCase.domino_1_1, MyTestCase.domino_1_1), True)

    def test_something_2(self):
        self.assertEqual(e4.can_be_fit(MyTestCase.domino_1_1, MyTestCase.domino_3_4), False)

    def test_something_3(self):
        self.assertEqual(e4.can_be_fit(MyTestCase.domino_1_2, MyTestCase.domino_2_5), True)

    def test_something_4(self):
        self.assertEqual(e4.can_be_fit(MyTestCase.domino_1_1, MyTestCase.domino_4_4), False)


if __name__ == '__main__':
    unittest.main()
