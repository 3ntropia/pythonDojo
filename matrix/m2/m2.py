"""
Para cada una de las siguientes matrices, desarrollar una función que la genere y
escribir un programa que invoque a cada una de ellas y muestre por pantalla la
matriz obtenida. El tamaño de las matrices debe establecerse como N x N, y las
funciones deben servir aunque este valor se modifique.
a:  1 0 0 0      b: 0 0 0 27         c: 4 0 0 0
    0 3 0 0         0 0 9 0             3 3 0 0
    0 0 5 0         0 3 0 0             2 2 2 0
    0 0 0 7         1 0 0 0             1 1 1 1

d:  8 8 8 8       e: 0 1 0 2           f: 0 0 0 1
    4 4 4 4          3 0 4 0              0 0 3 2
    2 2 2 2          0 5 0 6              0 6 5 4
    1 1 1 1          7 0 8 0              10 9 8 7

g:  1 2 3 4       h: 1 2 4 7             i: 1 2 6 7
    12 13 14         5 3 5 8             11 3 5 8 13
    11 16 15         6 6 9 12            14 4 9 12 14
    10 9 8 7         10 13 15            16 10 11 15 16"""


def first_matrix(size):
    m = []
    num = 1
    for i in range(size):
        m.append([num if y == i else 0 for y in range(size)])
        num += 2
    return m


def second_matrix(size):
    m = []
    num = 1
    for i in range(size):
        m.insert(0, [num if y == i else 0 for y in range(size)])
        num *= 3
    return m


def third_matrix(size):
    m = []
    num = size
    for i in range(size):
        m.append([num if y <= i else 0 for y in range(size)])
        num -= 1
    return m


def fourth_matrix(size):
    m = []
    num = size * 2
    for i in range(size):
        m.append([int(num) for _ in range(size)])
        num /= 2
    return m


def fifth_matrix(size):
    m = []
    num = 1
    for i in range(size):
        if i % 2 == 0:
            m.append([num if y % 2 != 0 else 0 for y in range(size)])
        else:
            m.append([num if y % 2 == 0 else 0 for y in range(size)])
        num += 1
    return m


if __name__ == "__main__":
    m1 = first_matrix(4)
    print(m1)
    m2 = second_matrix(4)
    print(m2)
    m3 = third_matrix(4)
    print(m3)
    m4 = fourth_matrix(4)
    print(m4)
    m5 = fifth_matrix(4)
    print(m5)
