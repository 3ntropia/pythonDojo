"""Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200."""


def even_list():
    return [x for x in range(101, 200, 2)]


if __name__ == '__main__':
    print(even_list())
