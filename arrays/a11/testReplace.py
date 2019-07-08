import unittest
from arrays.a11 import a11

class MyTestCase(unittest.TestCase):

    __string = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón"

    def test_something(self):
        self.assertEqual(a11.replace_string(MyTestCase.__string),
                         "PlateroEsPequeño,Peludo,Suave;TanBlandoPorFuera,QueSeDiríaTodoDeAlgodón")


