"""Ídem anterior, pero determinando si los vectores son paralelos. Cuando dos vecto-
res son paralelos los cocientes de sus coordenadas correspondientes son iguales
entre sí. Ejemplo: U = (3,-1) y V = (-9,3)"""

_MIN_ERROR = 0.001


def is_parallel(vector1, vector2):
    return vector1[0] / vector2[0] == vector1[1] / vector2[1]


def is_parallel_without_equal(vector1, vector2):
    return abs(vector1[0] / vector2[0] - vector1[1] / vector2[1]) < _MIN_ERROR
