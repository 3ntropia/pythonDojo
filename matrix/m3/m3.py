"""Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N^2), de tal forma que ningún número se repita.
Imprimir la matriz por pantalla."""
from random import randint


def ensure_random_matrix(size, repeated):
    number = randint(0, size**2)
    while repeated.count(number) > 0:
        number = randint(0, size ** 2)
    repeated.append(number)
    return number


def create_matrix(size):
    m = []
    repeated = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(ensure_random_matrix(size, repeated))
        m.append(row)
    return m


if __name__ == "__main__":
    m1 = create_matrix(4)
    print(m1)