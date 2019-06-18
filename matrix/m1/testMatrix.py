import unittest
import matrix.m1.matrixOperation as o


class MyTestCase(unittest.TestCase):
    __m__ = [[1, 2, 3], [9, 8, 11], [33, 2, 5]]
    __m_sorted__ = [[1, 2, 3], [8, 9, 11], [2, 5, 33]]
    __m_i__ = [[1, 2, 3], [9, 8, 11], [33, 2, 5], [12, 55, 3], [12, 73, 99]]

    def test_get_column(self):
        self.assertEqual(o.get_column(MyTestCase.__m__, 1), [2, 8, 2])

    def test_get_column_irregular_matrix(self):
        self.assertEqual(o.get_column(MyTestCase.__m_i__, 1), [2, 8, 2, 55, 73])

    def test_replace_column(self):
        mm = o.replace_column(MyTestCase.__m__, 1, [2, 3, 4])
        self.assertEqual(o.get_column(mm, 1), [2, 3, 4])

    def test_order_column(self):
        self.assertEqual(o.get_column(o.order_column(MyTestCase.__m__, 1), 1), [2, 2, 8])

    def test_order_row(self):
        self.assertEqual(o.sort_row(MyTestCase.__m__, 1), [8, 9, 11])

    def test_order_matrix_rows(self):
        self.assertEqual(o.sort_whole_matrix_row(MyTestCase.__m__), MyTestCase.__m_sorted__)

    def test_change_rows(self):
        self.assertEqual(o.change_row(MyTestCase.__m__, 0, 1), [[9, 8, 11], [1, 2, 3], [33, 2, 5]])

    def test_change_columns(self):
        self.assertEqual(o.change_column(MyTestCase.__m__, 0, 1), [[2, 1, 3], [8, 9, 11], [2, 33, 5]])

    def test_row_to_column(self):
        self.assertEqual(o.change_row_to_column(MyTestCase.__m__, 0, 0), [[1, 2, 3], [2, 8, 11], [3, 2, 5]])

    def test_transpose(self):
        self.assertEqual(o.transpose_matrix(MyTestCase.__m__), [[1, 9, 33], [2, 8, 2], [3, 11, 5]])

    def test_is_regular(self):
        self.assertEqual(o.is_regular(MyTestCase.__m__), True)

    def test_is_iregular(self):
        self.assertEqual(o.is_regular(MyTestCase.__m_i__), False)

    def test_is_not_simetric_regular(self):
        self.assertEqual(o.is_simetric(MyTestCase.__m__), False)

    def test_is_not_simetric_not_regular(self):
        self.assertEqual(o.is_simetric(MyTestCase.__m_i__), False)

    def test_is_simetric(self):
        self.assertEqual(o.is_simetric([[1, 2], [2, 3]]), True)

    def test_inversed_transposed(self):
        self.assertEqual(o.inversed_transpose_matrix([[1, 2], [3, 1]]), [[1, 2], [3, 1]])

    def test_is_secundary_simetric(self):
        self.assertEqual(o.is_secundary_simetric([[1, 2], [3, 1]]), True)

    def test_is_secundary_simetric_regular(self):
        self.assertEqual(o.is_secundary_simetric(MyTestCase.__m__), False)

    def test_is_secundary_simetric_not_regular(self):
        self.assertEqual(o.is_secundary_simetric(MyTestCase.__m_i__), False)


if __name__ == '__main__':
    unittest.main()
